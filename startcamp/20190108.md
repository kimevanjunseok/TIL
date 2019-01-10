### 클론후처리

`                                                                        
student@DESKTOP MINGW64 ~                                                       
$ cd Desktop/                                                                   
student@DESKTOP MINGW64 ~/Desktop                                               
$ cd junseok/                                                                   
student@DESKTOP MINGW64 ~/Desktop/junseok                                       
$ git credential reject                                                         
protocol=https                                                                  
host=github.com                                                                 
student@DESKTOP MINGW64 ~/Desktop/junseok                                       
$                                                                               
student@DESKTOP MINGW64 ~/Desktop/junseok                                       
$ cd TIL/                                                                       
student@DESKTOP MINGW64 ~/Desktop/junseok/TIL (master)                          
$ git push                                                                      
Everything up-to-date                                                           `

다른 방법 -> 제어판 -> 사용자계정 -> 자격증명관리 -> 윈도우 자격증명-> git삭제



`student@DESKTOP MINGW64 ~/Desktop/junseok/TIL (master)                          
$ git config --global user.name 'kimevanjunseok'                                
student@DESKTOP MINGW64 ~/Desktop/junseok/TIL (master)                          
$ git config -- global user.email jnunseok@gmail.com                            
error: key does not contain a section: global                                   
student@DESKTOP MINGW64 ~/Desktop/junseok/TIL (master)                          
$ git config --global user.email jnunseok@gmail.com                             
student@DESKTOP MINGW64 ~/Desktop/junseok/TIL (master)                          
$ git config --global --list                                                    
user.name=kimevanjunseok                                                        
user.email=jnunseok@gmail.com                                                   
core.autocrlf=true                                                              `

연수원 : TIL git push

집 : git pull/ add commit push

연수원 : git pull