LINKS:
https://create.arduino.cc/projecthub/rowan07/make-a-simple-led-circuit-ce8308
https://forum.arduino.cc/t/using-outputs-pins-as-ground/239267/2
https://www.arduino.cc/reference/en/language/functions/time/millis/
https://www.arduino.cc/reference/en/language/functions/digital-io/digitalwrite/
https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button
https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial
https://docs.arduino.cc/built-in-examples/basics/Blink
https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/
https://electronics.stackexchange.com/questions/34815/using-4-digit-7-segment-led
https://makbit.com/web/firmware/how-to-drive-4-digit-7-segment-led-display-with-arduino/
https://haneefputtur.com/7-segment-4-digit-led-display-sma420564-using-arduino.html


// ------------------------------- CONSTANTS -------------------------------


// Output pins.
const int PIN_DIGITS[4] = { 12, 2, 3, 4 };
const int PIN_SEGMENTS[7] = { 5, 6, 7, 8, 9, 10, 11 };
const int PIN_DP = 13;

// Input pins.
const int PIN_MENU = A0;
const int PIN_START = A1;
const int PIN_ADJUST = A2;
const int PIN_LED = A3;

// Segment states for each value.
const int NUMBERS[10][7] = {
  { HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW },
  { LOW, HIGH, HIGH, LOW, LOW, LOW, LOW },
  { HIGH, HIGH, LOW, HIGH, HIGH, LOW, HIGH },
  { HIGH, HIGH, HIGH, HIGH, LOW, LOW, HIGH },
  { LOW, HIGH, HIGH, LOW, LOW, HIGH, HIGH },
  { HIGH, LOW, HIGH, HIGH, LOW, HIGH, HIGH },
  { HIGH, LOW, HIGH, HIGH, HIGH, HIGH, HIGH },
  { HIGH, HIGH, HIGH, LOW, LOW, LOW, LOW },
  { HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH },
  { HIGH, HIGH, HIGH, HIGH, LOW, HIGH, HIGH },
};

// Button IDs.
const int MENU = 0;
const int START = 1;

// Button states.
const int EMPTY = 0;
const int DUNNO = 1;
const int CLICK = 2;
const int HOLD = 3;
const int TOO_MUCH = 4;

// Time necessary for a click to become a hold.
const int HOLD_DURATION = 1000;

// Mode IDs.
const int CLOCK = 0;
const int TIMER = 1;
const int STOPWATCH = 2;


// ------------------------------- STATE -------------------------------


// Button data.
int buttonState[2];
unsigned long releasedLastMillis[2];

// Clock data.
bool clockAdjusting, clockChanged;
int clockHours, clockMinutes;
unsigned long clockLastMillis;

// Timer data.
bool timerAdjusting, timerChanged, timerActive;
int timerMinutes, timerSeconds;
unsigned long timerLastMillis;

// Stopwatch data.
bool stopwatchActive;
int stopwatchMinutes, stopwatchSeconds;
unsigned long stopwatchLastMillis;

// Current mode.
int mode;


// ------------------------- DISPLAY FUNCTIONS -------------------------


// Enables one digit and disables the others.
void setDigit(int digit) {
  for (int i = 0; i < 4; i++) {
    if (i == digit)
      digitalWrite(PIN_DIGITS[i], LOW);
    else
      digitalWrite(PIN_DIGITS[i], HIGH);
  }
}

// Enables the segments necessary for displaying a value from 0 to 9.
void setSegments(int value) {
  for (int i = 0; i < 7; i++)
    digitalWrite(PIN_SEGMENTS[i], NUMBERS[value][i]);
}

// Enables or disables the decimal place.
void setDecimalPlace(bool enabled) {
  if (enabled)
    digitalWrite(PIN_DP, HIGH);
  else
    digitalWrite(PIN_DP, LOW);
}

// Clears the 7-segment display.
void clearDisplay() {
  for (int i = 0; i < 4; i++)
    digitalWrite(PIN_DIGITS[i], HIGH);
}

// Refreshes the 7-segment display.
void refreshDisplay(int digits[4], int dp) {
  for (int i = 0; i < 4; i++) {
    setDigit(i);
    setSegments(digits[i]);
    setDecimalPlace(i == dp);
    delay(2);
    setDecimalPlace(false);
  }
}

// ------------------------- BUTTON FUNCTIONS -------------------------

// Updates a button's state.
void updateButton(int id, int pin) {
  if (buttonState[id] == CLICK) {
    buttonState[id] = EMPTY;
  } else if (buttonState[id] == HOLD) {
    buttonState[id] = TOO_MUCH;
  }

  if (digitalRead(pin) == HIGH) {
    if (buttonState[id] == EMPTY) {
      buttonState[id] = DUNNO;
    }

    if (buttonState[id] == DUNNO && millis() - releasedLastMillis[id] >= HOLD_DURATION) {
      buttonState[id] = HOLD;
    }
  } else {
    if (buttonState[id] == DUNNO) {
      buttonState[id] = CLICK;
    } else if (buttonState[id] == TOO_MUCH) {
      buttonState[id] = EMPTY;
    }

    releasedLastMillis[id] = millis();
  }
}


// ------------------------- CLOCK FUNCTIONS -------------------------


// Increments the clock time by one minute.
void incrementClock() {
  clockMinutes++;
  if (clockMinutes == 60) {
    clockMinutes = 0;
    clockHours += 1;
    if (clockHours == 24) {
      clockHours = 0;
    }
  }
}

// Decrements the clock time by one minute.
void decrementClock() {
  clockMinutes--;
  if (clockMinutes == -1) {
    clockMinutes = 59;
    clockHours -= 1;
    if (clockHours == -1) {
      clockHours = 23;
    }
  } 
}

// Updates the clock mode.
void updateClock() {
  // Check if one minute has elapsed.
  if (millis() - clockLastMillis >= 60000) {
    incrementClock();
    clockLastMillis += 60000;
  }
}

// Called when the clock mode is selected.
void selectClock() {
  // Handle input.
  if (clockAdjusting) {
    if (buttonState[MENU] == CLICK) {
      clockAdjusting = false;
    }

    int input = analogRead(PIN_ADJUST) - 512;
    bool inTimeInterval = false;
    int timeStep = 0;

    if (input < -400 || input > 400) {
      inTimeInterval = ((millis() / 10) % 2 == 0);   
      timeStep = 2;     
    } else if (input < -300 || input > 300) {
      inTimeInterval = ((millis() / 10) % 2 == 0);
      timeStep = 1;
    } else if (input < -200 || input > 200) {
      inTimeInterval = ((millis() / 50) % 2 == 0);
      timeStep = 1;
    } else if (input < -100 || input > 100) {
      inTimeInterval = ((millis() / 200) % 2 == 0);
      timeStep = 1;
    }

    if (inTimeInterval && clockChanged == false) {
      for (int i = 0; i < timeStep; i++) {
        if (input < -100) {
          decrementClock(); 
        } else if (input > 100) {
          incrementClock();
        }
      }

      clockChanged = true;
    } else if (!inTimeInterval) {
      clockChanged = false;
    }

    digitalWrite(PIN_LED, HIGH);
  } else {
    if (buttonState[MENU] == HOLD) {
      clockAdjusting = true;
    } else if (buttonState[MENU] == CLICK) {
      mode = TIMER;
    }
    
    digitalWrite(PIN_LED, LOW);
  }

  // Display time.
  int digits[4] = {
    clockHours / 10,
    clockHours % 10,
    clockMinutes / 10,
    clockMinutes % 10
  };

  refreshDisplay(digits, 1);
}


// ------------------------- TIMER FUNCTIONS ------------------------


// Increments the timer time by one second.
void incrementTimer() {
  timerSeconds++;
  if (timerSeconds == 60) {
    timerSeconds = 0;
    timerMinutes += 1;
    if (timerMinutes == 60) {
      timerMinutes = 0;
    }
  }
}

// Decrements the timer time by one minute.
void decrementTimer() {
  timerSeconds--;
  if (timerSeconds == -1) {
    timerSeconds = 59;
    timerMinutes -= 1;
    if (timerMinutes == -1) {
      timerMinutes = 59;
    }
  } 
}

// Updates the timer mode.
void updateTimer() {
  if (!timerAdjusting && timerActive) {
    // Check if one second has elapsed.
    if (millis() - timerLastMillis >= 1000) {
      if (timerMinutes == 0 && timerSeconds == 0) {
        mode = TIMER;
      } else {
        decrementTimer();
        timerLastMillis += 1000;
      }
    }
  }
}

// Called when the timer mode is selected.
void selectTimer() {
  bool shouldBlink = false;
  
  if (timerAdjusting) {
    if (buttonState[MENU] == CLICK) {
      timerAdjusting = false;
      timerActive = true;
      timerLastMillis = millis();
    }

    int input = analogRead(PIN_ADJUST) - 512;
    bool inTimeInterval = false;
    int timeStep = 0;
  
    if (input < -400 || input > 400) {
      inTimeInterval = ((millis() / 10) % 2 == 0);   
      timeStep = 2;     
    } else if (input < -300 || input > 300) {
      inTimeInterval = ((millis() / 10) % 2 == 0);
      timeStep = 1;
    } else if (input < -200 || input > 200) {
      inTimeInterval = ((millis() / 50) % 2 == 0);
      timeStep = 1;
    } else if (input < -100 || input > 100) {
      inTimeInterval = ((millis() / 200) % 2 == 0);
      timeStep = 1;
    }
  
    if (inTimeInterval && timerChanged == false) {
      for (int i = 0; i < timeStep; i++) {
        if (input < -100) {
          decrementTimer(); 
        } else if (input > 100) {
          incrementTimer();
        }
      }
  
      timerChanged = true;
    } else if (!inTimeInterval) {
      timerChanged = false;
    }

    digitalWrite(PIN_LED, HIGH);
  } else {
    if (buttonState[MENU] == HOLD) {
      timerAdjusting = true;
    } else if (buttonState[MENU] == CLICK) {
      mode = STOPWATCH;

      if (timerMinutes == 0 && timerSeconds == 0) {
        timerActive = false;
      }
    }

    if (timerMinutes == 0 && timerSeconds == 0) {
      shouldBlink = true;
    }

    digitalWrite(PIN_LED, LOW);
  }

  // Display time.
  int digits[4] = {
    timerMinutes / 10,
    timerMinutes % 10,
    timerSeconds / 10,
    timerSeconds % 10
  };

  if (shouldBlink && (millis() / 500) % 2 == 0) {
    clearDisplay();
  } else {
    refreshDisplay(digits, 1);
  }
}


// ----------------------- STOPWATCH FUNCTIONS ----------------------

// Increments the stopwatch time by one second.
void incrementStopwatch() {
  stopwatchSeconds++;
  if (stopwatchSeconds == 60) {
    stopwatchSeconds = 0;
    stopwatchMinutes += 1;
    if (stopwatchMinutes == 60) {
      stopwatchMinutes = 0;
    }
  }
}

// Updates the stopwatch mode.
void updateStopwatch() {
  if (stopwatchActive) {
    // Check if one second has elapsed.
    if (millis() - stopwatchLastMillis >= 1000) {
      incrementStopwatch();
      stopwatchLastMillis += 1000;
    }
  }
}

// Called when the stopwatch mode is selected.
void selectStopwatch() {
  if (!stopwatchActive) {
    if (buttonState[START] == CLICK) {
      stopwatchActive = true;
      stopwatchLastMillis = millis();
    }

    if (buttonState[START] == HOLD) {
      stopwatchMinutes = 0;
      stopwatchSeconds = 0;
    }
  } else {
    if (buttonState[START] == CLICK)
      stopwatchActive = false;
  }

  if (buttonState[MENU] == CLICK)
    mode = CLOCK;

  // Display time.
  int digits[4] = {
    stopwatchMinutes / 10,
    stopwatchMinutes % 10,
    stopwatchSeconds / 10,
    stopwatchSeconds % 10
  };
  
  refreshDisplay(digits, 1);
}


// ------------------------- MAIN FUNCTIONS -------------------------


void setup() {
  for (int i = 0; i < 4; i++)
    pinMode(PIN_DIGITS[i], OUTPUT);
  for (int i = 0; i < 7; i++)
    pinMode(PIN_SEGMENTS[i], OUTPUT);
  pinMode(PIN_DP, OUTPUT);

  pinMode(PIN_MENU, INPUT);
  pinMode(PIN_START, INPUT);

  buttonState[MENU] = EMPTY;
  buttonState[START] = EMPTY;
  releasedLastMillis[MENU] = 0;
  releasedLastMillis[START] = 0;

  clockAdjusting = false;
  clockChanged = false;
  clockHours = 0;
  clockMinutes = 0;
  clockLastMillis = 0;

  timerAdjusting = false;
  timerActive = false;
  timerMinutes = 0;
  timerSeconds = 0;
  timerLastMillis = 0;

  stopwatchActive = false;
  stopwatchMinutes = 0;
  stopwatchSeconds = 0;
  stopwatchLastMillis = 0;
  
  mode = CLOCK;
}

void loop() {
  updateButton(MENU, PIN_MENU);
  updateButton(START, PIN_START);

  updateClock();
  updateTimer();
  updateStopwatch();

  if (mode == CLOCK)
    selectClock();
  else if (mode == TIMER)
    selectTimer();
  else
    selectStopwatch();
}
