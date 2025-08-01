import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QTimer, Qt
import struct   

class STMEmulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STM Emulator")
        self.setGeometry(200, 200, 400, 200)

        self.serial = QSerialPort()
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_next_command)

        self.commands = {
            "CMD_OVERVOLTAGE_24V":     bytearray([0x71, 0x02, 0x04, 0x42, 0x0f, 0x5c, 0x29, 0xe2, 0x77]),  # 35.89 V
            "CMD_OVERVOLTAGE_12V":     bytearray([0x71, 0x04, 0x04, 0x41, 0xa0, 0x00, 0x00, 0xe8, 0x77]),  # 20.0 V
            "CMD_OVERVOLTAGE_5V":      bytearray([0x71, 0x06, 0x04, 0x41, 0x20, 0x00, 0x00, 0xca, 0x77]),  # 10.0 V
            "CMD_UNDERVOLTAGE_24V":    bytearray([0x71, 0x08, 0x04, 0x41, 0x10, 0x66, 0x66, 0xcf, 0x77]),  # 9.05 V

            "CMD_UNDERVOLTAGE_12V":    bytearray([0x71, 0x0A, 0x04, 0x40, 0xe0, 0x00, 0x00, 0xbe, 0x77]),  # 7.0 V
            "CMD_UNDERVOLTAGE_5V":     bytearray([0x71, 0x0C, 0x04, 0x40, 0xa0, 0x00, 0x00, 0xba, 0x77]),  # 5.0 V
            "CMD_OVERCURRENT_24V":     bytearray([0x71, 0x0E, 0x04, 0x3f, 0x80, 0x00, 0x00, 0xa1, 0x77]),  # 1.0 A
            "CMD_OVERCURRENT_12V":     bytearray([0x71, 0x10, 0x04, 0x3f, 0x40, 0x00, 0x00, 0xf3, 0x77]),  # 0.75 A

            "CMD_OVERCURRENT_5V":      bytearray([0x71, 0x12, 0x04, 0x3f, 0x00, 0x00, 0x00, 0x87, 0x77]),  # 0.5 A
            "CMD_OVERCURRENT_IN1":     bytearray([0x71, 0x14, 0x04, 0x3e, 0xcc, 0xcc, 0xcd, 0x9e, 0x77]),  # 0.4 A
            "CMD_OVERCURRENT_IN2":     bytearray([0x71, 0x16, 0x04, 0x3e, 0x99, 0x99, 0x9a, 0x95, 0x77]),  # 0.3 A
            "CMD_OVERCURRENT_IN3":     bytearray([0x71, 0x18, 0x04, 0x3e, 0x4c, 0xcc, 0xcd, 0xa3, 0x77]),  # 0.2 A

            "CMD_OVERCURRENT_IN4":     bytearray([0x71, 0x1A, 0x04, 0x3e, 0x19, 0x99, 0x9a, 0xa6, 0x77]),  # 0.15 A
            "CMD_OVERTEMP_24V":        bytearray([0x71, 0x1C, 0x04, 0x42, 0x04, 0x00, 0x00, 0xc4, 0x77]),  # 33.0 °C
            "CMD_OVERTEMP_12V":        bytearray([0x71, 0x1E, 0x04, 0x41, 0xf0, 0x00, 0x00, 0xd1, 0x77]),  # 30.0 °C
            "CMD_OVERTEMP_5V":         bytearray([0x71, 0x20, 0x04, 0x41, 0xc8, 0x00, 0x00, 0xf2, 0x77]),  # 25.0 °C

            "CMD_OVERTEMP_PROBE1":     bytearray([0x71, 0x22, 0x04, 0x41, 0xa0, 0x00, 0x00, 0xe6, 0x77]),  # 20.0 °C
            "CMD_OVERTEMP_PROBE2":     bytearray([0x71, 0x24, 0x04, 0x41, 0x80, 0x00, 0x00, 0xe9, 0x77]),  # 16.0 °C
            "CMD_OVERTEMP_CHIP":       bytearray([0x71, 0x26, 0x04, 0x41, 0x60, 0x00, 0x00, 0xec, 0x77]),  # 14.0 °C
            "CMD_UNDERTEMP_PROBE1":    bytearray([0x71, 0x28, 0x04, 0xc1, 0x20, 0x00, 0x00, 0x0c, 0x77]),  # -10.0 °C

            "CMD_UNDERTEMP_PROBE2":    bytearray([0x71, 0x2A, 0x04, 0xc1, 0x40, 0x00, 0x00, 0x1e, 0x77]),  # -12.0 °C
            "CMD_UNDERTEMP_CHIP":      bytearray([0x71, 0x2C, 0x04, 0xc1, 0x60, 0x00, 0x00, 0x30, 0x77]),  # -14.0 °C
            "Switch Command":          bytearray([0x71, 0x1D, 0x02, 0x10, 0x01, 0x30, 0x77]),  # Switch state  
        }


        self.command_keys = list(self.commands.keys())
        self.command_index = 0

        self.init_ui()

    def send_next_command(self):
        if not self.serial.isOpen() or not self.command_keys:
            return

        key = self.command_keys[self.command_index]
        data = self.commands[key]
        self.serial.write(data)

     
        raw_data_bytes = data[3:7]
        value = struct.unpack('>f', raw_data_bytes)[0]  

        print(f"Gönderildi: {key} → {data.hex().upper()} → Değer: {value:.2f}")

        self.command_index = (self.command_index + 1) % len(self.command_keys)

    def init_ui(self):
        layout = QVBoxLayout()

        self.portComboBox = QComboBox()
        self.load_ports()

        self.statusLabel = QLabel("Durum: Bağlı değil")
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.connectButton = QPushButton("Porta Bağlan")
        self.connectButton.clicked.connect(self.toggle_connection)

        self.startButton = QPushButton("Gönderimi Başlat")
        self.startButton.clicked.connect(self.start_sending)
        self.startButton.setEnabled(False)

        self.stopButton = QPushButton("Durdur")
        self.stopButton.clicked.connect(self.stop_sending)
        self.stopButton.setEnabled(False)

        layout.addWidget(self.portComboBox)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.connectButton)
        layout.addWidget(self.startButton)
        layout.addWidget(self.stopButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_ports(self):
        self.portComboBox.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.portComboBox.addItem(port.portName())

    def toggle_connection(self):
        if self.serial.isOpen():
            self.serial.close()
            self.statusLabel.setText("❌ Port kapatıldı.")
            self.connectButton.setText("Porta Bağlan")
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(False)
        else:
            port_name = self.portComboBox.currentText()
            self.serial.setPortName(port_name)
            self.serial.setBaudRate(115200)
            self.serial.setDataBits(QSerialPort.Data8)
            self.serial.setParity(QSerialPort.NoParity)
            self.serial.setStopBits(QSerialPort.OneStop)
            self.serial.setFlowControl(QSerialPort.NoFlowControl)

            if self.serial.open(QSerialPort.WriteOnly):
                self.statusLabel.setText(f"✅ Bağlandı: {port_name}")
                self.connectButton.setText("Portu Kapat")
                self.startButton.setEnabled(True)
            else:
                self.statusLabel.setText("❌ Bağlantı hatası!")

    def start_sending(self):
        if self.serial.isOpen():
            self.command_index = 0
            self.timer.start(500)
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)
            self.statusLabel.setText("📤 Gönderim başladı...")

    def stop_sending(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.statusLabel.setText("⏸ Gönderim durduruldu.")

    def send_next_command(self):
        if not self.serial.isOpen() or not self.command_keys:
            return

        key = self.command_keys[self.command_index]
        data = self.commands[key]
        self.serial.write(data)
        print(f"Gönderildi: {key} → {data.hex()}")

        self.command_index = (self.command_index + 1) % len(self.command_keys)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = STMEmulator()
    window.show()
    sys.exit(app.exec_())
