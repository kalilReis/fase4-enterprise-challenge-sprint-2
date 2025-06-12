#include <DHTesp.h>

// Pin definitions
#define DHT_PIN   15   // DHT22 data pin


DHTesp dht;

void setup() {
  Serial.begin(115200);
  dht.setup(DHT_PIN, DHTesp::DHT22);

 
}

void loop() {
  // Read sensors
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();

  // Print readings
  Serial.printf(
    "Temp: %.1f°C, Umid: %.1f%%\n",
    temperature,
    humidity
  );


  delay(2000);  // Wait 2 seconds between readings
}
