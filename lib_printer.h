/***************************************************************************
* Nom du fichier:
* Description	: 
*
* Auteur	: 
* Créé le	:
* Compilateur	: 
***************************************************************************
* Modifié le  	:
***************************************************************************/

#include <xc.h>

#ifndef FCY
#define FCY 4000000UL
#endif
#include <libpic30.h>

//------------------------------------------------------------------------------
#define PRINTER_UART   2
//-----------------------------------------------------------------------------
#if (PRINTER_UART == 1)
    #define PRN_UXBRG   U1BRG
    #define PRN_UXMODE  U1MODE
    #define PRN_UXSTA   U1STA
    #define PRN_BFBIT   U1STAbits.UTXBF
    #define PRN_UXTXREG U1TXREG
    #define PRN_RXIE    IEC0bits.U1RXIE 
    #define PRN_RXISR   _U1RXInterrupt 
    #define PRN_UXRXREG U1RXREG
    #define PRN_RXIF    IFS0bits.U1RXIF  
#elif (PRINTER_UART == 2)
    #define PRN_UXBRG   U2BRG
    #define PRN_UXMODE  U2MODE
    #define PRN_UXSTA   U2STA
    #define PRN_BFBIT   U2STAbits.UTXBF
    #define PRN_UXTXREG U2TXREG
    #define PRN_RXIE    IEC1bits.U2RXIE 
    #define PRN_RXISR   _U2RXInterrupt
    #define PRN_UXRXREG U2RXREG
    #define PRN_RXIF    IFS1bits.U2RXIF
#elif (PRINTER_UART == 3)
    #define PRN_UXBRG   U3BRG
    #define PRN_UXMODE  U3MODE
    #define PRN_UXSTA   U3STA
    #define PRN_BFBIT   U3STAbits.UTXBF
    #define PRN_UXTXREG U3TXREG
    #define PRN_RXIE    IEC5bits.U3RXIE 
    #define PRN_RXISR   _U3RXInterrupt
    #define PRN_UXRXREG U3RXREG
    #define PRN_RXIF    IFS5bits.U3RXIF
#elif (PRINTER_UART == 4)
    #define PRN_UXBRG   U4BRG
    #define PRN_UXMODE  U4MODE
    #define PRN_UXSTA   U4STA
    #define PRN_BFBIT   U4STAbits.UTXBF
    #define PRN_UXTXREG U4TXREG
    #define PRN_RXIE    IEC5bits.U4RXIE 
    #define PRN_RXISR   _U4RXInterrupt
    #define PRN_UXRXREG U4RXREG
    #define PRN_RXIF    IFS5bits.U4RXIF
#endif
//------------------------------------------------------------------------------

#define     PRN_ESC     0x1B        // Escape
#define     PRN_DC2     0x12

#define     PRN_LF      0x0A        // Line Feed
#define     PRN_HT      0x09        // Jump next tab pos

#define     PRN_PRINT_TEST_PAGE     0x54

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    printer_init(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    printer_putch(uint8_t Byte);  

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    printer_puts(uint8_t *pStr);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    printer_print_test_page(void);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    printer_print(uint8_t *pStr);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/





