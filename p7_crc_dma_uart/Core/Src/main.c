/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2025 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

#define RX_BUFFER_SIZE 50
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE BEGIN PD */

uint32_t data_packet[7];
uint32_t data_packet2[16];


uint8_t Tdata[6];
uint8_t Rdata[6];

uint8_t TX_Buffer[50];
uint8_t RX_Buffer[50];

uint32_t crc;
uint32_t crc1;
uint32_t gelen_crc;
uint32_t hesaplanan_crc;
uint32_t crc_check;

uint32_t command = 0x05;
uint32_t size = 0x0A;
uint8_t data[16];

uint8_t i;
uint8_t buton = 0;
uint8_t buton1 = 0;
uint8_t durum;


HAL_StatusTypeDef Status1;
HAL_StatusTypeDef Status2;


uint8_t aRXBufferUser[RX_BUFFER_SIZE];  // DMA RX hedefi
uint8_t UserBuffer1[RX_BUFFER_SIZE];
uint8_t UserBuffer2[RX_BUFFER_SIZE];

uint8_t *pBufferReadyForUser = UserBuffer1;
uint8_t *pBufferReadyForReception = UserBuffer2;

uint16_t uwNbReceivedChars = 0;

/* USER CODE END PD */


/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
CRC_HandleTypeDef hcrc;

UART_HandleTypeDef huart1;
DMA_HandleTypeDef hdma_usart1_rx;
DMA_HandleTypeDef hdma_usart1_tx;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_CRC_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */


/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */

int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_USART1_UART_Init();
  MX_CRC_Init();
  /* USER CODE BEGIN 2 */
  if (command >= 0x01 && command <= 0x22)
    {
      if (size >= 0x01 && size <= 0x10)
      {
        data_packet[0] = command;
        data_packet[1] = size;
        data_packet[2] = 0x05;
        data_packet[3] = 0x0A;
        data_packet[4] = 0x05;
        data_packet[5] = 0x02;
        data_packet[6] = 0x01;

        crc = HAL_CRC_Calculate(&hcrc, data_packet, 2 + size);

        TX_Buffer[0] = 0x0B;
        TX_Buffer[1] = command;
        TX_Buffer[2] = size;

        TX_Buffer[3] = (crc >> 24) & 0xFF;
        TX_Buffer[4] = (crc >> 16) & 0xFF;
        TX_Buffer[5] = (crc >> 8) & 0xFF;
        TX_Buffer[6] = (crc >> 0) & 0xFF;
        TX_Buffer[7] = 0x09;



        HAL_UART_Transmit_DMA(&huart1, TX_Buffer, 8);

        HAL_UARTEx_ReceiveToIdle_DMA(&huart1, aRXBufferUser, RX_BUFFER_SIZE);


      }
    }


  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */

  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE3);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief CRC Initialization Function
  * @param None
  * @retval None
  */
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
    static uint16_t old_pos = 0;
    uint8_t *ptemp;
    uint8_t i;

    if (huart->Instance == USART1)
    {
        if (Size != old_pos)
        {
            if (Size > old_pos)
            {
                uwNbReceivedChars = Size - old_pos;
                for (i = 0; i < uwNbReceivedChars; i++)
                {
                    pBufferReadyForUser[i] = aRXBufferUser[old_pos + i];
                }
            }
            else
            {
                uwNbReceivedChars = RX_BUFFER_SIZE - old_pos;
                for (i = 0; i < uwNbReceivedChars; i++)
                {
                    pBufferReadyForUser[i] = aRXBufferUser[old_pos + i];
                }
                if (Size > 0)
                {
                    for (i = 0; i < Size; i++)
                    {
                        pBufferReadyForUser[uwNbReceivedChars + i] = aRXBufferUser[i];
                    }
                    uwNbReceivedChars += Size;
                }
            }


            if (pBufferReadyForUser[0] == 0x0B)
            {
                size = pBufferReadyForUser[2];
                memset(data_packet2, 0, sizeof(data_packet2));
                for (uint8_t j = 0; j < size + 2 ; j++)
                {
                    data_packet2[j] = pBufferReadyForUser[1 + j];
                }

                crc1 = HAL_CRC_Calculate(&hcrc, data_packet2, 2 + size);

                gelen_crc = (pBufferReadyForUser[3 + size] << 24) |
                            (pBufferReadyForUser[4 + size] << 16) |
                            (pBufferReadyForUser[5 + size] << 8) |
                            (pBufferReadyForUser[6 + size]);

                if (crc1 == gelen_crc)
                {

                }
                else
                {

                }
            }



            ptemp = pBufferReadyForUser;
            pBufferReadyForUser = pBufferReadyForReception;
            pBufferReadyForReception = ptemp;


        }
        old_pos = 0;
        HAL_UARTEx_ReceiveToIdle_DMA(&huart1, aRXBufferUser, RX_BUFFER_SIZE);
    }
}

static void MX_CRC_Init(void)
{

  /* USER CODE BEGIN CRC_Init 0 */

  /* USER CODE END CRC_Init 0 */

  /* USER CODE BEGIN CRC_Init 1 */

  /* USER CODE END CRC_Init 1 */
  hcrc.Instance = CRC;
  if (HAL_CRC_Init(&hcrc) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN CRC_Init 2 */

  /* USER CODE END CRC_Init 2 */

}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 115200;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * Enable DMA controller clock
  */
static void MX_DMA_Init(void)
{

  /* DMA controller clock enable */
  __HAL_RCC_DMA2_CLK_ENABLE();

  /* DMA interrupt init */
  /* DMA2_Stream2_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA2_Stream2_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA2_Stream2_IRQn);
  /* DMA2_Stream7_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA2_Stream7_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA2_Stream7_IRQn);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  /* USER CODE BEGIN MX_GPIO_Init_1 */

  /* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /* USER CODE BEGIN MX_GPIO_Init_2 */

  /* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
