from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5 import QtGui
import sys
import struct


class MySwitch(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setMinimumWidth(90)
        self.setMinimumHeight(25)
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid black;
                border-radius: 10px;
                background-color: gray;
                color: white;
                font-weight: bold;
            }
            QPushButton:checked {
                background-color: green;
            }
        """)

    def paintEvent(self, event):
        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.gray
        

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(center)

        painter.setBrush(QtGui.QBrush(bg_color))
        pen = QtGui.QPen(Qt.black)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRoundedRect(QRect(-width, -radius, 2 * width, 2 * radius), radius, radius)

        painter.setBrush(QtGui.QBrush(Qt.blue))
        sw_rect = QRect(-radius, -radius, width + radius, 2 * radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)

        painter.setPen(Qt.white)
        painter.drawText(sw_rect, Qt.AlignCenter, label)

class MyComboBox(QComboBox):
    
    def enterEvent(self, event):
        if self.load_ports_callback:
            self.load_ports_callback()
        super().enterEvent(event)


class SerialCommandSender(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Command Sender")
        self.setGeometry(100, 100, 900, 700)

        self.serial = QSerialPort()
        self.serial.readyRead.connect(self.receive_data)
        

        self.commands = {
            "Read_Voltage_24V": bytearray([0x71, 0x00, 0x01, 0x00, 0x01, 0x77]),  # 24V start
            "Read_Current_24V": bytearray([0x71, 0x01, 0x01, 0x00, 0x02, 0x77]),
            "Read_OverVoltage_24V": bytearray([0x71, 0x02, 0x01, 0x00, 0x03, 0x77]),
            "Read_UnderVoltage_24V": bytearray([0x71, 0x03, 0x01, 0x00, 0x04, 0x77]),
            "Read_OverCurrent_24V": bytearray([0x71, 0x04, 0x01, 0x00, 0x05, 0x77]),
            "Read_OverTemperature_24V": bytearray([0x71, 0x05, 0x01, 0x00, 0x06, 0x77]),  # 24V end

            "Read_Voltage_12V": bytearray([0x71, 0x06, 0x01, 0x00, 0x07, 0x77]),  # 12V start
            "Read_Current_12V": bytearray([0x71, 0x07, 0x01, 0x00, 0x08, 0x77]),
            "Read_OverVoltage_12V": bytearray([0x71, 0x08, 0x01, 0x00, 0x09, 0x77]),
            "Read_UnderVoltage_12V": bytearray([0x71, 0x09, 0x01, 0x00, 0x0A, 0x77]),
            "Read_OverCurrent_12V": bytearray([0x71, 0x0A, 0x01, 0x00, 0x0B, 0x77]),
            "Read_OverTemperature_12V": bytearray([0x71, 0x0B, 0x01, 0x00, 0x0C, 0x77]),  # 12V end

            "Read_Voltage_5V": bytearray([0x71, 0x0C, 0x01, 0x00, 0x0D, 0x77]),  # 5V start
            "Read_Current_5V": bytearray([0x71, 0x0D, 0x01, 0x00, 0x0E, 0x77]),
            "Read_OverVoltage_5V": bytearray([0x71, 0x0E, 0x01, 0x00, 0x0F, 0x77]),
            "Read_UnderVoltage_5V": bytearray([0x71, 0x0F, 0x01, 0x00, 0x10, 0x77]),
            "Read_OverCurrent_5V": bytearray([0x71, 0x10, 0x01, 0x00, 0x11, 0x77]),
            "Read_OverTemperature_5V": bytearray([0x71, 0x11, 0x01, 0x00, 0x12, 0x77]),  # 5V end

            "Read_Temperature_MCU": bytearray([0x71, 0x12, 0x01, 0x00, 0x13, 0x77]),  # MCU Start

            "Read_OverTemperature_MCU": bytearray([0x71, 0x13, 0x01, 0x00, 0x14, 0x77]),
            "Read_UnderTemperature_MCU": bytearray([0x71, 0x14, 0x01, 0x00, 0x15, 0x77]),  # MCU end

            "Read_Temperature_P1": bytearray([0x71, 0x15, 0x01, 0x00, 0x16, 0x77]),  # Probe1 start
            "Read_OverTemperature_P1": bytearray([0x71, 0x16, 0x01, 0x00, 0x17, 0x77]),
            "Read_UnderTemperature_P1": bytearray([0x71, 0x17, 0x01, 0x00, 0x18, 0x77]),  # Probe1 end

            "Read_Temperature_P2": bytearray([0x71, 0x18, 0x01, 0x00, 0x19, 0x77]),  # probe2 start
            "Read_OverTemperature_P2": bytearray([0x71, 0x19, 0x01, 0x00, 0x1A, 0x77]),
            "Read_UnderTemperature_P2": bytearray([0x71, 0x1A, 0x01, 0x00, 0x1B, 0x77]),  # probe2 end

            "Read_Alert": bytearray([0x71, 0x1B, 0x01, 0x00, 0x1C, 0x77]),  # alert
            "Read_Switch_Status": bytearray([0x71, 0x1C, 0x02, 0x00, 0x00, 0x1E, 0x77]),
        }

        self.command_labels = {
            0x02: "Over Voltage 24V",
            0x04: "Over Voltage 12V",
            0x06: "Over Voltage 5V",
            0x08: "Under Voltage 24V",
            0x0A: "Under Voltage 12V",
            0x0C: "Under Voltage 5V",
            0x0E: "Over Current 24V",
            0x10: "Over Current 12V",
            0x12: "Over Current 5V",
            0x14: "Over Current 12V Input 1",
            0x16: "Over Current 12V Input 2",
            0x18: "Over Current 12V Input 3",
            0x1A: "Over Current 12V Input 4",
            0x1C: "Over Temperature 24V",
            0x1E: "Over Temperature 12V",
            0x20: "Over Temperature 5V",
            0x22: "Over Temperature Prop One",
            0x24: "Over Temperature Prop Two",
            0x26: "Over Temperature Chip",
            0x28: "Under Temperature Prop One",
            0x2A: "Under Temperature Prop Two",
            0x2C: "Under Temperature Chip",
            0x2E: "I2C Communication Error",
            0x30: "Reserved",
        }

        self.command_keys = list(self.commands.keys())
        self.command_index = 0
        self.init_ui()
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_next_command)

    def init_ui(self):
            central = QWidget()
            self.setCentralWidget(central)
            main_layout = QVBoxLayout()

            top_bar = QHBoxLayout()
            self.portComboBox = MyComboBox(self)
            self.portComboBox.load_ports_callback = self.load_ports
            self.load_ports()
            self.portComboBox.setMinimumWidth(150)
           #self.portComboBox.view().pressed.connect(lambda _: self.load_ports())

            top_bar.addWidget(QLabel("🔌 Port:"))
            top_bar.addWidget(self.portComboBox)
            top_bar.addSpacing(20)
            self.connectButton = QPushButton("🔗 Bağlan")
            self.connectButton.setMinimumWidth(60)
            self.connectButton.clicked.connect(self.connect_serial)
            top_bar.addWidget(self.connectButton)
            self.statusLabel = QLabel("")
            self.statusLabel.setStyleSheet("font-weight: bold; color: green;")
            top_bar.addWidget(self.statusLabel)
            top_bar.addStretch()
            self.sendLabel = QLabel("")
            self.sendLabel.setStyleSheet("color: orange; font-weight: bold;")
            top_bar.addWidget(self.sendLabel)
            main_layout.addLayout(top_bar)

            switch_group = QGroupBox("🧭 Switch Kontrolleri")
            switch_layout = QGridLayout()
            self.switch_checkboxes = []
            input_labels = ["12V Input 1", "12V Input 2", "12V Input 3", "12V Input 4",
                            "5V Input 1", "5V Input 2", "5V Input 3", "5V Input 4",
                            "5V Input 5", "5V Input 6", ]
            
            self.switch_checkboxes = []
            self.led_indicators = []

            self.switch_timer = QTimer()
            self.switch_timer.timeout.connect(self.send_switch_command)


            for i, label in enumerate(input_labels):
                sw = MySwitch()
                sw.setChecked(False)
                sw.setToolTip(label)
                sw.toggled.connect(self.send_switch_command)

                self.switch_checkboxes.append(sw)

                led = QLabel()
                led.setFixedSize(15, 15)
                led.setStyleSheet("border-radius: 7px; background-color: gray; border: 1px solid black;")
                self.led_indicators.append(led)

                row = (i // 5) * 2
                col = i % 5


                hbox = QHBoxLayout()
                hbox.addWidget(sw)
                hbox.addWidget(led)
                hbox.setAlignment(Qt.AlignCenter)

                container = QWidget()
                container.setLayout(hbox)

                switch_layout.addWidget(container, row, col)

                lbl = QLabel(label)
                lbl.setAlignment(Qt.AlignCenter)
                switch_layout.addWidget(lbl, row + 1, col)
            switch_group.setLayout(switch_layout)
            main_layout.addWidget(switch_group)



            middle_layout = QHBoxLayout()

            sensor_group = QGroupBox("📊 Sensor Values")

            sensor_group_layout = QVBoxLayout(sensor_group)

            self.tx_label = QLabel("TX: ")
            self.tx_label.setStyleSheet("font-weight: bold; color: blue;")

            self.rx_label = QLabel("RX: ")
            self.rx_label.setStyleSheet("font-weight: bold; color: purple;")

            tx_rx_layout = QHBoxLayout()
            tx_rx_layout.addWidget(self.tx_label)
            tx_rx_layout.addStretch()
            tx_rx_layout.addWidget(self.rx_label)

            sensor_group_layout.addLayout(tx_rx_layout)

            
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            sensor_container = QWidget()
            sensor_layout = QGridLayout(sensor_container)

            sensor_layout.setHorizontalSpacing(2)  
            sensor_layout.setVerticalSpacing(0)    
            
            
            self.sensor_widgets = {}
            def add_sensor_widget(row, col, label_text, cmd_type, unit=""):
                label = QLabel(label_text)
                label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                label.setStyleSheet("font-size: 12px; font-weight: bold;")

                lcd = QLCDNumber()
                lcd.setDigitCount(7)
                lcd.setSegmentStyle(QLCDNumber.Flat)
                lcd.setFixedSize(130, 35)
                
                lcd.setStyleSheet("color: #00FF00; background-color: black; border: 2px solid gray;")
                lcd.display(0)

                unit_label = QLabel(unit)
                unit_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                unit_label.setStyleSheet("font-size: 17px; font-weight: bold; padding: 0px;")

                lcd_layout = QHBoxLayout()
                lcd_layout.setContentsMargins(0, 0, 0, 0)
                lcd_layout.setSpacing(0)
                lcd_layout.addWidget(lcd)
                lcd_layout.addWidget(unit_label)

                lcd_container = QWidget()
                lcd_container.setLayout(lcd_layout)
                

                sensor_layout.addWidget(label, row * 2, col)
                sensor_layout.addWidget(lcd_container, row * 2 + 1, col)  

                self.sensor_widgets[cmd_type] = lcd


            add_sensor_widget(0, 0, "Over Voltage \n24V", 0x02,"V")
            add_sensor_widget(0, 1, "Over Voltage \n12V", 0x04,"V")
            add_sensor_widget(0, 2, "Over Voltage \n5V", 0x06,"V")
            add_sensor_widget(0, 3, "Under Voltage \n24V", 0x08,"V")

            add_sensor_widget(1, 0, "Under Voltage \n12V", 0x0A,"V")
            add_sensor_widget(1, 1, "Under Voltage \n5V", 0x0C,"V")
            add_sensor_widget(1, 2, "Over Current \n24V", 0x0E,"A")
            add_sensor_widget(1, 3, "Over Current \n12V", 0x10,"A")

            add_sensor_widget(2, 0, "Over Current \n5V", 0x12,"A")
            add_sensor_widget(2, 1, "Over Current \n12V Input 1", 0x14,"A")
            add_sensor_widget(2, 2, "Over Current \n12V Input 2", 0x16,"A")
            add_sensor_widget(2, 3, "Over Current \n12V Input 3", 0x18,"A")

            add_sensor_widget(3, 0, "Over Current \n12V Input 4", 0x1A,"A")
            add_sensor_widget(3, 1, "Over Temp \n24V", 0x1C,"°C")
            add_sensor_widget(3, 2, "Over Temp \n12V", 0x1E,"°C")
            add_sensor_widget(3, 3, "Over Temp \n5V", 0x20,"°C")

            add_sensor_widget(4, 0, "Over Temp \nProbe1", 0x22,"°C")
            add_sensor_widget(4, 1, "Over Temp \nProbe2", 0x24,"°C")
            add_sensor_widget(4, 2, "Over Temp \nChip", 0x26,"°C")
            add_sensor_widget(4, 3, "Under Temp \nProbe1", 0x28,"°C")

            add_sensor_widget(5, 0, "Under Temp \nProbe2", 0x2A,"°C")
            add_sensor_widget(5, 1, "Under Temp \nChip", 0x2C,"°C")


            scroll.setWidget(sensor_container)
   

            
            sensor_group_layout.addWidget(scroll)

            tx_rx_layout = QHBoxLayout()
            tx_rx_layout.addWidget(self.tx_label)
            tx_rx_layout.addStretch()
            tx_rx_layout.addWidget(self.rx_label)

            sensor_group_layout.addLayout(tx_rx_layout)

            
            right_box = QVBoxLayout()
            
           

            middle_layout.addWidget(sensor_group, stretch=10)

            main_layout.addLayout(middle_layout)

            

            central.setLayout(main_layout)


    def reset_leds_to_gray(self):
        for led in self.led_indicators:
            led.setStyleSheet("border-radius: 7px; background-color: gray; border: 1px solid black;")



    def load_ports(self):
        current_port = self.portComboBox.currentText()  
        self.portComboBox.clear()
        ports = QSerialPortInfo.availablePorts()
        port_names = [port.portName() for port in ports]
        self.portComboBox.addItems(port_names)
     
        if current_port in port_names:
            index = port_names.index(current_port)
            self.portComboBox.setCurrentIndex(index)
        else:
           
            if port_names:
                self.portComboBox.setCurrentIndex(0)


    def connect_serial(self):
        if self.serial.isOpen():
            self.serial.close()
            self.connectButton.setText("Bağlan")
            self.timer.stop()
            self.statusLabel.setText("")
            self.sendLabel.setText("")

            #for led in self.led_indicators:
             #   led.setStyleSheet("border-radius: 7px; background-color: gray; border: 1px solid black;")


            return
        port_name = self.portComboBox.currentText()
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(115200)
        self.serial.setDataBits(QSerialPort.Data8)
        self.serial.setParity(QSerialPort.NoParity)
        self.serial.setStopBits(QSerialPort.OneStop)
        self.serial.setFlowControl(QSerialPort.NoFlowControl)
        if self.serial.open(QSerialPort.ReadWrite):
            self.connectButton.setText("Kes")
            self.statusLabel.setText(f"Bağlandı: {port_name}")
            self.timer.start(100)

        else:
            self.statusLabel.setText("Bağlantı hatası")


    def send_next_command(self):
            if not self.serial.isOpen():
                return
            self.sendLabel.setText("📤 Veriler gönderiliyor...")
            for key in self.command_keys:
                packet = self.commands[key]
                self.serial.write(packet)
                tx_binary = ' '.join(format(b, '08b') for b in packet)
                self.tx_label.setText(f"TX: {tx_binary}")



    def update_leds_from_switch_value(self, switch_value):
        for i in range(len(self.led_indicators)):
            state = (switch_value >> i) & 1  # 0 veya 1
            color = "green" if state else "red"
            self.led_indicators[i].setStyleSheet(
                f"border-radius: 7px; background-color: {color}; border: 1px solid black;"
            )
            self.switch_checkboxes[i].blockSignals(True)
            self.switch_checkboxes[i].setChecked(state == 1)
            self.switch_checkboxes[i].blockSignals(False)
            


    def send_switch_command(self):
        if not self.serial.isOpen():
            return

        switch_value = 0
        for i, cb in enumerate(self.switch_checkboxes):
            if cb.isChecked():
                switch_value |= (1 << i)
                
        data_low = switch_value & 0xFF
        data_high = (switch_value >> 8) & 0xFF


        checksum = (0x1D + 2 + data_low + data_high) & 0xFF
        packet = bytearray([0x71, 0x1D, 0x02, data_low, data_high, checksum, 0x77])
        
        self.serial.write(packet)

        self.update_leds_from_switch_value(switch_value)


      
        #for led in self.led_indicators:
            #led.setStyleSheet("border-radius: 7px; background-color: red; border: 1px solid black;")

 




    def update_led(self, index, state):
        if 0 <= index < len(self.led_indicators):
            color = "green" if state else "red"
            self.led_indicators[index].setStyleSheet(
                f"border-radius: 7px; background-color: {color}; border: 1px solid black;"
            )

    def receive_data(self):
        ERROR_STATUS_MAP = {0: "Unread Error", 1: "No Error", 2: "Error Present"}

        while self.serial.bytesAvailable() >= 3:
            header = self.serial.read(1)
            if header[0] != 0x71:
                continue  

            cmd = self.serial.read(1)
            length_byte = self.serial.read(1)
            length = length_byte[0]

            total_remaining = length + 1 + 1  
            while self.serial.bytesAvailable() < total_remaining:
                return 

            body = self.serial.read(total_remaining)
            data = header + cmd + length_byte + body

            if data[-1] != 0x77:
                hex_data = data.hex(' ')

                continue

            cmd_val = cmd[0]
            payload = data[3:3+length]
            rx_binary = ' '.join(format(b, '08b') for b in data)
            self.rx_label.setText(f"RX: {rx_binary}")


            checksum = data[-2]

            try:
                if cmd_val == 0x1D and length == 2:
                    switch_value = payload[0] | (payload[1] << 8)

                    self.update_leds_from_switch_value(switch_value)
                elif length == 4:
                    value = struct.unpack('>f', payload)[0]
                    label = self.command_labels.get(cmd_val, f"Unknown CMD 0x{cmd_val:02X}")

                    lcd = self.sensor_widgets.get(cmd_val)
                    if lcd:
                        lcd.display(f"{value:.3f}")
            except Exception as e:
                print(f"Hata oluştu: {e}")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialCommandSender()
    window.show()
    sys.exit(app.exec_())
