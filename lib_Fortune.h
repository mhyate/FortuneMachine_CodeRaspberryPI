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
#define FCY 4000000UL
#include <libpic30.h>

#include <stdio.h>

#include    "lib_GPS.h"  
#include    "lib_printer.h"
#include    "lib_coin_accept.h"
#include    "lib_com.h"


#define     MISC0        LATAbits.LATA0
#define     TRIS_MISC0   TRISAbits.TRISA0

#define     MISC1        LATAbits.LATA1
#define     TRIS_MISC1   TRISAbits.TRISA1

#define     MISC2        LATBbits.LATB10
#define     TRIS_MISC2   TRISBbits.TRISB10

#define     MISC3        LATBbits.LATB11
#define     TRIS_MISC3   TRISBbits.TRISB11

#define     FORCE_SEND_GPS  10      // Nombre de trames en provenance GPS à recevoir avant de forcer une émission vers l'IHM


/*--------------------------------------------------------------------------*/
/* Fonction  : void Initialiser(void)    									*/
/* Description : Configuration ressources                                   */
/* PE : Aucune                                                              */
/* ps : Aucune                                                              */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void Initialiser(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/





