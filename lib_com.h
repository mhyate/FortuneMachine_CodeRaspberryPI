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
#include <stdio.h> 
#include <string.h>

#include "lib_GPS.h"

//-----------------------------------------------------------------------------
#define COM_UART   3
//-----------------------------------------------------------------------------
#if (COM_UART == 1)
    #define COM_UXBRG   U1BRG
    #define COM_UXMODE  U1MODE
    #define COM_UXSTA   U1STA
    #define COM_BFBIT   U1STAbits.UTXBF
    #define COM_UXTXREG U1TXREG
    #define COM_RXIE    IEC0bits.U1RXIE 
    #define COM_RXISR   _U1RXInterrupt 
    #define COM_UXRXREG U1RXREG
    #define COM_RXIF    IFS0bits.U1RXIF  
#elif (COM_UART == 2)
    #define COM_UXBRG   U2BRG
    #define COM_UXMODE  U2MODE
    #define COM_UXSTA   U2STA
    #define COM_BFBIT   U2STAbits.UTXBF
    #define COM_UXTXREG U2TXREG
    #define COM_RXIE    IEC1bits.U2RXIE 
    #define COM_RXISR   _U2RXInterrupt
    #define COM_UXRXREG U2RXREG
    #define COM_RXIF    IFS1bits.U2RXIF
#elif (COM_UART == 3)
    #define COM_UXBRG   U3BRG
    #define COM_UXMODE  U3MODE
    #define COM_UXSTA   U3STA
    #define COM_BFBIT   U3STAbits.UTXBF
    #define COM_UXTXREG U3TXREG
    #define COM_RXIE    IEC5bits.U3RXIE 
    #define COM_RXISR   _U3RXInterrupt  
    #define COM_UXRXREG U3RXREG
    #define COM_RXIF    IFS5bits.U3RXIF
#elif (COM_UART == 4)
    #define COM_UXBRG   U4BRG
    #define COM_UXMODE  U4MODE
    #define COM_UXSTA   U4STA
    #define COM_BFBIT   U4STAbits.UTXBF
    #define COM_UXTXREG U4TXREG
    #define COM_RXIE    IEC5bits.U4RXIE 
    #define COM_RXISR   _U4RXInterrupt
    #define COM_UXRXREG U4RXREG
    #define COM_RXIF    IFS5bits.U4RXIF
#endif
//-----------------------------------------------------------------------------
#ifndef RX_STATUS_TYPE
#define RX_STATUS_TYPE
typedef enum    {WAIT_START,RX_ON,WAIT_RD_BUFFER} tRxStatus;
#endif

#define COM_START       0x3C    // '<' character
#define COM_CR          0x0A

typedef enum {  FR_ERROR,
                FR_PRINT,
                FR_GET_GPS_DATE,
                FR_GET_GPS_POS} tRxTypeFrame;

#define     ID_UNKNOWN_FRAME        1
#define     ID_FRAME_ERROR          2
#define     ID_ERROR_COIN_ACCEPTOR  3

// Define some "boolean" values                
#define TRUE    1
#define FALSE   0

/*--------------------------------------------------------------------------*/
/* Description :                                                            */
/* PE : Aucune                                                              */
/* ps : Aucune                                                              */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void com_init(void);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_putch(uint8_t Byte);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_puts(uint8_t *pStr);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
uint8_t    com_check(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_clear(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_send_gps_pos(tRMC_MINIMAL_DATA *pData);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_send_gps_date(tRMC_MINIMAL_DATA *pData);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_send_coin_ok(uint8_t aCoinValue);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
tRxTypeFrame com_get_frame_type(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_send_info(uint8_t *apInfo);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    com_send_error(uint8_t aCode, uint8_t *apMsg);







