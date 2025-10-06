/*
 * delay.h
 *
 *  Created on: Sep 29, 2025
 *      Author: barki
 */

#ifndef INC_DELAY_H_
#define INC_DELAY_H_




#include "stm32f3xx.h"


// Set to "1" to use the inlined Delay_ms() function
#define DELAY_INLINE               1


// Public functions and macros

#if (DELAY_INLINE)
// Do a delay for a specified number of milliseconds
// input:
//   delay_counter - number of milliseconds to wait
__STATIC_INLINE void Delay_ms(__IO uint32_t delay_counter) {
    while (delay_counter) {
        if (SysTick->CTRL & SysTick_CTRL_COUNTFLAG_Msk) {
            delay_counter--;
        }
    }
}
#endif // DELAY_INLINE


// Function prototypes
void Delay_Init(void);
#if (!DELAY_INLINE)
void Delay_ms(uint32_t ms);
#endif // DELAY_INLINE


#endif /* INC_DELAY_H_ */
