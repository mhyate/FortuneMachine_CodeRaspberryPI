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
#include <string.h>

#ifndef LIB_GPS_H
#define LIB_GPS_H


//-----------------------------------------------------------------------------
#define GPS_UART   1
//-----------------------------------------------------------------------------
#if (GPS_UART == 1)
    #define GPS_UXBRG   U1BRG
    #define GPS_UXMODE  U1MODE
    #define GPS_UXSTA   U1STA
    #define GPS_BFBIT   U1STAbits.UTXBF
    #define GPS_UXTXREG U1TXREG
    #define GPS_RXIE    IEC0bits.U1RXIE 
    #define GPS_RXISR   _U1RXInterrupt 
    #define GPS_UXRXREG U1RXREG
    #define GPS_RXIF    IFS0bits.U1RXIF  
#elif (GPS_UART == 2)
    #define GPS_UXBRG   U2BRG
    #define GPS_UXMODE  U2MODE
    #define GPS_UXSTA   U2STA
    #define GPS_BFBIT   U2STAbits.UTXBF
    #define GPS_UXTXREG U2TXREG
    #define GPS_RXIE    IEC1bits.U2RXIE 
    #define GPS_RXISR   _U2RXInterrupt
    #define GPS_UXRXREG U2RXREG
    #define GPS_RXIF    IFS1bits.U2RXIF
#elif (GPS_UART == 3)
    #define GPS_UXBRG   U3BRG
    #define GPS_UXMODE  U3MODE
    #define GPS_UXSTA   U3STA
    #define GPS_BFBIT   U3STAbits.UTXBF
    #define GPS_UXTXREG U3TXREG
    #define GPS_RXIE    IEC5bits.U3RXIE 
    #define GPS_RXISR   _U3RXInterrupt
    #define GPS_UXRXREG U3RXREG
    #define GPS_RXIF    IFS5bits.U3RXIF
#elif (GPS_UART == 4)
    #define GPS_UXBRG   U4BRG
    #define GPS_UXMODE  U4MODE
    #define GPS_UXSTA   U4STA
    #define GPS_BFBIT   U4STAbits.UTXBF
    #define GPS_UXTXREG U4TXREG
    #define GPS_RXIE    IEC5bits.U4RXIE 
    #define GPS_RXISR   _U4RXInterrupt
    #define GPS_UXRXREG U4RXREG
    #define GPS_RXIF    IFS5bits.U4RXIF
#endif
//-----------------------------------------------------------------------------
#ifndef RX_STATUS_TYPE
#define RX_STATUS_TYPE
typedef enum    {WAIT_START,RX_ON,WAIT_RD_BUFFER} tRxStatus;
#endif

typedef enum    {GPS_RECEIVE_OFF,GPS_RECEIVE_ON} tGpsReceiveStatus;

typedef struct{
    // UTC date of the fix
    uint8_t   day; // Day of the month[0 -> 31]
    uint8_t   month; //  Month [1 -> 12]
    uint8_t   year; //  Year [00 -> 99] (2000 -> 2099)
    
    // UTC time of the fix
    uint8_t   hh; //  UTC Hours [0 -> 23]
    uint8_t   mm; //  UTC Minutes [0 -> 59]
    uint8_t   ss; //  UTC seconds [0 -> 59]
    
    // Latitude
    uint8_t   latDeg; // Latitude degrees
    uint8_t   latMin; // Latitude minutes
    unsigned int    latDec; // decimal part of minutes
    uint8_t   latNS;  // either 'N' = North or 'S' = South
    
    // Longitude
    uint8_t   longDeg; // Latitude degrees
    uint8_t   longMin; // Latitude minutes
    unsigned int    longDec; // decimal part of minutes
    uint8_t   longEW;  // either  either 'E' = East or 'W' = West
    
    // Validité données
    uint8_t   ValidData;  // either 'A' = Valid or 'V' not valid
    
} tRMC_MINIMAL_DATA;


#define NMEA_START  '$'
#define NMEA_CR     0x0D   // first car of the <CR><LF> sequence

#define NB_CHAMPS       15
#define TAILLE_CHAMP    16

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    gps_init(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
//void    gps_putch(uint8_t Byte);    

/*--------------------------------------------------------------------------*/
/* Fonction  :  gps_check                                                   */
/* Description :    Checks for pending GPS frame                            */
/* PE :   none                                                              */
/* ps :     0 (false): no pending frame                                     */
/*          1 (true) : one pending frame                                    */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
uint8_t    gps_check(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :  gps_clear                                                   */
/* Description :    clears the rxok flag                                    */
/* PE :   none                                                              */
/* ps :   none                                                              */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void            gps_clear(void);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps : 0 si trame pas RMC, 1 si trame RMC                                                                    */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
uint8_t   gps_decode(tRMC_MINIMAL_DATA *pData);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    gps_receive_on(void);
void    gps_receive_off(void);
tGpsReceiveStatus gps_get_receive_status(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
signed char     get2digits(uint8_t* pBuffer);
signed int      get3digits(uint8_t* pBuffer);
signed int      get4digits(uint8_t* pBuffer); 


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
signed char SplitTrame(uint8_t * pBuffer);




#endif

