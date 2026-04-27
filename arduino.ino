void setup() {
  Serial.begin(9600);
}

void loop() {
  // Leer LDR (0 = oscuro, 1023 = mucha luz)
  int lectura_ldr = analogRead(A0);
  
  // Convertir a porcentaje de luz (0% a 100%)
  float luz = (lectura_ldr / 1023.0) * 100.0;

  // Enviar por serial
  Serial.println(luz);

  delay(500); // cada medio segundo
}
