idea of project:
   
  we tried to implement online space_invader game using pygame and sockets

  each game has four players firing bullets against each other 

  the one with non_zero health at last will win the game



  How you tried to implement it:

     we wrote a server.py file which collects receives co_ordinates of each of 4_players 

     and sends them to other three players and the game.py script updates the co_ordinates 

     of each player in the game according to the values received by server


     the server.py file that we wrote can actually handle multiple games(4 members in each game)

     we achived this using threading



  Problems that we faced:

     we faced slightly laging issues while port_forwarding(using ngrok server)


     if we run these scripts on local_network there is no langing


  What you learnt from the project:

     1)handling_time



  Members of the project

  Team name = codingnoobs

  IMT2020545-PoorneshwarChaganti
  IMT2020555-Ayyappa koppauravuri


