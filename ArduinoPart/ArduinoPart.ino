//ByNick

/*⢰⣶⣶⣦⡀⠀⠀⠀⠀⢰⣶⣶⡆⠀⠀⠀⠀⢀⣴⣶⣶⡆
  ⢸⣿⣿⣿⣿⣦⠀⠀⠀⠸⠿⠿⠇⠀⠀⠀⣴⣿⣿⣿⣿⡇
  ⢸⣿⣿⣏⠙⢿⣷⣄⠀⢠⣤⣤⡄⠀⣠⣾⡿⠋⢸⣿⣿⡇
  ⢸⣿⣿⡇⠀⠀⠹⣿⣶⣸⣿⣿⣇⣶⣿⠏⠀⠀⢸⣿⣿⡇
  ⢸⣿⣿⣇⠀⣀⣀⠈⢿⣿⣿⣿⣿⡿⠁⣀⣀⠀⢸⣿⣿⡇
  ⢸⣿⣿⡇⣾⡟⠁⠀⠀⣹⣿⣿⣏⠀⠀⠈⢻⣷⢸⣿⣿⡇
  ⢸⣿⣿⣷⣿⠁⠀⢀⣼⣿⣿⣿⣿⣷⡀⠀⠈⣿⣾⣿⣿⡇
  ⢸⣿⣿⣿⣿⡀⣰⣿⠿⢹⣿⣿⡏⠿⣿⣆⢀⣿⣿⣿⣿⡇
  ⢸⣿⣿⡇⣿⣿⡿⠋⠀⢸⣿⣿⡇⠀⠙⢿⣿⣿⢸⣿⣿⡇
  ⢸⣿⣿⣿⣿⠿⣿⣦⣀⢸⣿⣿⡇⣀⣴⣿⠿⣿⣿⣿⣿⡇
  ⠸⠿⠿⠟⠁⠀⠈⠙⠻⠿⠿⠿⠿⠟⠋⠁⠀⠈⠻⠿⠿⠇
 */

const int TopLeft = 8;
const int TopRight = 9;
const int BottomLeft = 10;
const int BottomRight = 11;
int incomingByte;

void setup() {
 
  Serial.begin(9600);

  pinMode(TopLeft, OUTPUT);
  pinMode(TopRight, OUTPUT);
  pinMode(BottomLeft, OUTPUT);
  pinMode(BottomRight, OUTPUT);
  
}

void loop() {

  if (Serial.available()) {
    
    incomingByte = Serial.read();
    
    if (incomingByte == 'S') {
      
    }
   
}}

void Forward(){
  
  digitalWrite(TopLeft,HIGH);
  digitalWrite(TopRight,HIGH);
  digitalWrite(BottomLeft,HIGH);
  digitalWrite(BottomRight,HIGH);
  
}
void Left(){
  
  digitalWrite(TopLeft,LOW);
  digitalWrite(TopRight,HIGH);
  digitalWrite(BottomLeft,LOW);
  digitalWrite(BottomRight,HIGH);
  
}
void Right(){
  
  digitalWrite(TopLeft,HIGH);
  digitalWrite(TopRight,LOW);
  digitalWrite(BottomLeft,HIGH);
  digitalWrite(BottomRight,LOW);
  
}
void Stop(){
  
  digitalWrite(TopLeft,LOW);
  digitalWrite(TopRight,LOW);
  digitalWrite(BottomLeft,LOW);
  digitalWrite(BottomRight,LOW);
  
}
