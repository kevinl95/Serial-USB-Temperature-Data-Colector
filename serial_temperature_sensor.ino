void setup()
{
  Serial.begin(9600);  //Start the serial connection with the computer
                       //to view the result open the serial monitor 
}
 
void loop()
{
 int reading = analogRead(9);  
 
 // Teensy reference voltage is 3.3V
 float voltage = reading * 3.3;
 voltage /= 1024.0; 
 
 // now print out the temperature
 float temperatureC = (voltage - 0.5) * 100 ;  //converting from 10 mv per degree wit 500 mV offset
                                               //to degrees ((voltage - 500mV) times 100)
 Serial.print(temperatureC);
 // Print a space
 Serial.print(' ');
 // now convert to Fahrenheit
 float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
 Serial.print(temperatureF);
 // New line
 Serial.print('\n');
 
 delay(60000);                                     //waiting a minute
}
