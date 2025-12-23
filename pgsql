
---

## 3️⃣ ESP32 Sensor Node Code (`esp32_sensor_node.ino`)

```cpp
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11
#define GAS_SENSOR 34

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  int gas = analogRead(GAS_SENSOR);

  Serial.print(temp);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(gas);

  delay(2000);
}
