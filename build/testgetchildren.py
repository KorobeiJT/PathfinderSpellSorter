import tkinter
import tkinter.ttk

TKI_Principal = tkinter.Tk ( )
BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )
LAB_Enfant = tkinter.Label ( TKI_Principal )
TRV_Pays = tkinter.ttk.Treeview ( TKI_Principal , columns = ( "Capitale" ) )

TRV_Pays.column ( "#0" , width = 150 , minwidth = 100 , stretch = False )
TRV_Pays.column ( "Capitale" , width = 100 , minwidth = 100 , stretch = False )
TRV_Pays.heading ( "#0" , text = "Pays" , anchor = "w" )
TRV_Pays.heading ( "Capitale" , text = "Capitale" , anchor = "center" )

TRV_Pays.insert ( "" , 1 , "L01" , text = "Canada" , values = ( "Quebec" ) )
TRV_Pays.insert ( "" , 2 , "L02" , text = "Suisse" , values = ( "Berne" ) )
TRV_Pays.insert ( "" , 3 , "L03" , text = "Belgique" , values = ( "Bruxelles" ) )
TRV_Pays.insert ( "" , 4 , "L04" , text = "Liban" , values = ( "Beyrouth" ) )
TRV_Pays.insert ( "" , 5 , "L05" , text = "Chine" , values = ( "Pekin" ) )
TRV_Pays.insert ( "L05" , 6 , "L06" , text = "Chine" , values = ( str(len(TRV_Pays.get_children ('L05')))) )


TRV_Pays.pack ( )
LAB_Enfant.pack ( )
BUT_Quitter.pack ( )

LAB_Enfant [ "text" ] = f"{ TRV_Pays.get_children ('L05') } "
print(len(TRV_Pays.get_children ('L06')))

TKI_Principal.mainloop ( )