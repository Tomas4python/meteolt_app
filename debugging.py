# Module used for manual review of data, when length of data received differs from standard

l1 = [{'airTemperature': 19.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.1,
  'forecastTimeUtc': '2023-08-29 08:00:00',
  'relativeHumidity': 75,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 73,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 20.7,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 20.7,
  'forecastTimeUtc': '2023-08-29 09:00:00',
  'relativeHumidity': 71,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 75,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 22.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 22.4,
  'forecastTimeUtc': '2023-08-29 10:00:00',
  'relativeHumidity': 64,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 71,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 23.6,
  'cloudCover': 99,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 23.5,
  'forecastTimeUtc': '2023-08-29 11:00:00',
  'relativeHumidity': 58,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 81,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 24.4,
  'cloudCover': 99,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 24.4,
  'forecastTimeUtc': '2023-08-29 12:00:00',
  'relativeHumidity': 56,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 91,
  'windGust': 11,
  'windSpeed': 5},
 {'airTemperature': 24.8,
  'cloudCover': 98,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 24.8,
  'forecastTimeUtc': '2023-08-29 13:00:00',
  'relativeHumidity': 56,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 98,
  'windGust': 11,
  'windSpeed': 5},
 {'airTemperature': 25.5,
  'cloudCover': 17,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 25.5,
  'forecastTimeUtc': '2023-08-29 14:00:00',
  'relativeHumidity': 54,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 105,
  'windGust': 11,
  'windSpeed': 5},
 {'airTemperature': 25.5,
  'cloudCover': 76,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 25.6,
  'forecastTimeUtc': '2023-08-29 15:00:00',
  'relativeHumidity': 58,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 106,
  'windGust': 10,
  'windSpeed': 4},
 {'airTemperature': 24.9,
  'cloudCover': 3,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 25.1,
  'forecastTimeUtc': '2023-08-29 16:00:00',
  'relativeHumidity': 63,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 94,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 23.6,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 23.8,
  'forecastTimeUtc': '2023-08-29 17:00:00',
  'relativeHumidity': 70,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 79,
  'windGust': 7,
  'windSpeed': 3},
 {'airTemperature': 22.2,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 22.2,
  'forecastTimeUtc': '2023-08-29 18:00:00',
  'relativeHumidity': 73,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 83,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 21.5,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 21.5,
  'forecastTimeUtc': '2023-08-29 19:00:00',
  'relativeHumidity': 75,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 88,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 20.9,
  'cloudCover': 58,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 20.9,
  'forecastTimeUtc': '2023-08-29 20:00:00',
  'relativeHumidity': 77,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 91,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 20.5,
  'cloudCover': 89,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 20.5,
  'forecastTimeUtc': '2023-08-29 21:00:00',
  'relativeHumidity': 79,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 96,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 20.3,
  'cloudCover': 91,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 20.3,
  'forecastTimeUtc': '2023-08-29 22:00:00',
  'relativeHumidity': 80,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 96,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 20.8,
  'cloudCover': 76,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 20.8,
  'forecastTimeUtc': '2023-08-29 23:00:00',
  'relativeHumidity': 79,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 110,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 21.8,
  'cloudCover': 44,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 21.8,
  'forecastTimeUtc': '2023-08-30 00:00:00',
  'relativeHumidity': 74,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 156,
  'windGust': 7,
  'windSpeed': 4},
 {'airTemperature': 22.8,
  'cloudCover': 15,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 22.8,
  'forecastTimeUtc': '2023-08-30 01:00:00',
  'relativeHumidity': 64,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 164,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 22.7,
  'cloudCover': 93,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 22.7,
  'forecastTimeUtc': '2023-08-30 02:00:00',
  'relativeHumidity': 59,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 172,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 22.3,
  'cloudCover': 98,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 22.3,
  'forecastTimeUtc': '2023-08-30 03:00:00',
  'relativeHumidity': 58,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 169,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 22.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 22.5,
  'forecastTimeUtc': '2023-08-30 04:00:00',
  'relativeHumidity': 56,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 162,
  'windGust': 8,
  'windSpeed': 5},
 {'airTemperature': 23.7,
  'cloudCover': 23,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 23.6,
  'forecastTimeUtc': '2023-08-30 05:00:00',
  'relativeHumidity': 56,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 163,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 25.2,
  'cloudCover': 46,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 25.1,
  'forecastTimeUtc': '2023-08-30 06:00:00',
  'relativeHumidity': 52,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 164,
  'windGust': 11,
  'windSpeed': 6},
 {'airTemperature': 26.8,
  'cloudCover': 74,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 27.1,
  'forecastTimeUtc': '2023-08-30 07:00:00',
  'relativeHumidity': 47,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 171,
  'windGust': 12,
  'windSpeed': 6},]
l2 = [
 {'airTemperature': 28.4,
  'cloudCover': 7,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 28.2,
  'forecastTimeUtc': '2023-08-30 08:00:00',
  'relativeHumidity': 42,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 190,
  'windGust': 11,
  'windSpeed': 4},
 {'airTemperature': 29.9,
  'cloudCover': 5,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 29,
  'forecastTimeUtc': '2023-08-30 09:00:00',
  'relativeHumidity': 34,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 183,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 31.3,
  'cloudCover': 70,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 31.3,
  'forecastTimeUtc': '2023-08-30 10:00:00',
  'relativeHumidity': 26,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 174,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 32.2,
  'cloudCover': 87,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 32.2,
  'forecastTimeUtc': '2023-08-30 11:00:00',
  'relativeHumidity': 21,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 173,
  'windGust': 11,
  'windSpeed': 5},
 {'airTemperature': 32.6,
  'cloudCover': 24,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 32.6,
  'forecastTimeUtc': '2023-08-30 12:00:00',
  'relativeHumidity': 18,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0,
  'windDirection': 171,
  'windGust': 12,
  'windSpeed': 5},
 {'airTemperature': 32,
  'cloudCover': 86,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 32,
  'forecastTimeUtc': '2023-08-30 13:00:00',
  'relativeHumidity': 24,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0,
  'windDirection': 177,
  'windGust': 12,
  'windSpeed': 5},
 {'airTemperature': 31.6,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 31.6,
  'forecastTimeUtc': '2023-08-30 14:00:00',
  'relativeHumidity': 26,
  'seaLevelPressure': 1001,
  'totalPrecipitation': 0,
  'windDirection': 176,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 30.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 29.5,
  'forecastTimeUtc': '2023-08-30 15:00:00',
  'relativeHumidity': 33,
  'seaLevelPressure': 1000,
  'totalPrecipitation': 0,
  'windDirection': 154,
  'windGust': 13,
  'windSpeed': 7},
 {'airTemperature': 23.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 23.4,
  'forecastTimeUtc': '2023-08-30 16:00:00',
  'relativeHumidity': 59,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0,
  'windDirection': 231,
  'windGust': 24,
  'windSpeed': 6},
 {'airTemperature': 20.7,
  'cloudCover': 100,
  'conditionCode': 'heavy-rain-with-thunderstorms',
  'feelsLikeTemperature': 20.7,
  'forecastTimeUtc': '2023-08-30 17:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 6,
  'windDirection': 161,
  'windGust': 11,
  'windSpeed': 6},
 {'airTemperature': 20.1,
  'cloudCover': 100,
  'conditionCode': 'heavy-rain',
  'feelsLikeTemperature': 20.1,
  'forecastTimeUtc': '2023-08-30 18:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 4,
  'windDirection': 278,
  'windGust': 13,
  'windSpeed': 2},
 {'airTemperature': 19.8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.8,
  'forecastTimeUtc': '2023-08-30 19:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 118,
  'windGust': 4,
  'windSpeed': 1},
 {'airTemperature': 19.6,
  'cloudCover': 73,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 19.6,
  'forecastTimeUtc': '2023-08-30 20:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 151,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 19.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.3,
  'forecastTimeUtc': '2023-08-30 21:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 172,
  'windGust': 6,
  'windSpeed': 2},
 {'airTemperature': 19.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.2,
  'forecastTimeUtc': '2023-08-30 22:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 178,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 19.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.1,
  'forecastTimeUtc': '2023-08-30 23:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 193,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 19,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19,
  'forecastTimeUtc': '2023-08-31 00:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 191,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 18.9,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 18.9,
  'forecastTimeUtc': '2023-08-31 01:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 1.1,
  'windDirection': 200,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 19,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19,
  'forecastTimeUtc': '2023-08-31 02:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 210,
  'windGust': 6,
  'windSpeed': 2},
 {'airTemperature': 19.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 19.1,
  'forecastTimeUtc': '2023-08-31 03:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 236,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 18.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 18.9,
  'forecastTimeUtc': '2023-08-31 04:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 253,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 18.8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 18.8,
  'forecastTimeUtc': '2023-08-31 05:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 271,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 17.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 17.9,
  'forecastTimeUtc': '2023-08-31 06:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 282,
  'windGust': 6,
  'windSpeed': 3},]
l3 = [
 {'airTemperature': 20.9,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 20.9,
  'forecastTimeUtc': '2023-08-31 09:00:00',
  'relativeHumidity': 81,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0.3,
  'windDirection': 242,
  'windGust': 8,
  'windSpeed': 3},
 {'airTemperature': 21,
  'cloudCover': 86,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 21,
  'forecastTimeUtc': '2023-08-31 12:00:00',
  'relativeHumidity': 81,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 1.8,
  'windDirection': 265,
  'windGust': 7,
  'windSpeed': 3},
 {'airTemperature': 19.2,
  'cloudCover': 79,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 19.2,
  'forecastTimeUtc': '2023-08-31 15:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 4.6,
  'windDirection': 252,
  'windGust': 5,
  'windSpeed': 1},
 {'airTemperature': 17.4,
  'cloudCover': 91,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 17.4,
  'forecastTimeUtc': '2023-08-31 18:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0.3,
  'windDirection': 219,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': 16.3,
  'cloudCover': 41,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 16.3,
  'forecastTimeUtc': '2023-08-31 21:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 251,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 15.8,
  'cloudCover': 99,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 15.8,
  'forecastTimeUtc': '2023-09-01 00:00:00',
  'relativeHumidity': 98,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 4.8,
  'windDirection': 230,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 15.4,
  'cloudCover': 99,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 15.4,
  'forecastTimeUtc': '2023-09-01 03:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 2.9,
  'windDirection': 236,
  'windGust': 7,
  'windSpeed': 4},
 {'airTemperature': 14.9,
  'cloudCover': 60,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 14.9,
  'forecastTimeUtc': '2023-09-01 06:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0.9,
  'windDirection': 242,
  'windGust': 11,
  'windSpeed': 5},]
l4 = [
 {'airTemperature': 17.4,
  'cloudCover': 12,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 17.4,
  'forecastTimeUtc': '2023-09-01 09:00:00',
  'relativeHumidity': 68,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0.2,
  'windDirection': 243,
  'windGust': 12,
  'windSpeed': 6},
 {'airTemperature': 18.6,
  'cloudCover': 22,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 18.6,
  'forecastTimeUtc': '2023-09-01 12:00:00',
  'relativeHumidity': 54,
  'seaLevelPressure': 1012,
  'totalPrecipitation': 0,
  'windDirection': 237,
  'windGust': 13,
  'windSpeed': 7},
 {'airTemperature': 18,
  'cloudCover': 90,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 18,
  'forecastTimeUtc': '2023-09-01 15:00:00',
  'relativeHumidity': 53,
  'seaLevelPressure': 1012,
  'totalPrecipitation': 0,
  'windDirection': 231,
  'windGust': 12,
  'windSpeed': 6},
 {'airTemperature': 14.9,
  'cloudCover': 19,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 14.9,
  'forecastTimeUtc': '2023-09-01 18:00:00',
  'relativeHumidity': 70,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0,
  'windDirection': 227,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 12.5,
  'cloudCover': 96,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 12.5,
  'forecastTimeUtc': '2023-09-01 21:00:00',
  'relativeHumidity': 85,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 216,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 12.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 12.5,
  'forecastTimeUtc': '2023-09-02 00:00:00',
  'relativeHumidity': 86,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 211,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 12.9,
  'cloudCover': 26,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 12.9,
  'forecastTimeUtc': '2023-09-02 03:00:00',
  'relativeHumidity': 83,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0.2,
  'windDirection': 219,
  'windGust': 10,
  'windSpeed': 6},
 {'airTemperature': 14.8,
  'cloudCover': 23,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 14.8,
  'forecastTimeUtc': '2023-09-02 06:00:00',
  'relativeHumidity': 76,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 226,
  'windGust': 13,
  'windSpeed': 6},]
l5 = [
 {'airTemperature': 18.2,
  'cloudCover': 90,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 18.2,
  'forecastTimeUtc': '2023-09-02 09:00:00',
  'relativeHumidity': 63,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 245,
  'windGust': 14,
  'windSpeed': 7},
 {'airTemperature': 18.8,
  'cloudCover': 57,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 18.8,
  'forecastTimeUtc': '2023-09-02 12:00:00',
  'relativeHumidity': 63,
  'seaLevelPressure': 1015,
  'totalPrecipitation': 0.4,
  'windDirection': 253,
  'windGust': 15,
  'windSpeed': 7},
 {'airTemperature': 17.7,
  'cloudCover': 65,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 17.7,
  'forecastTimeUtc': '2023-09-02 15:00:00',
  'relativeHumidity': 73,
  'seaLevelPressure': 1015,
  'totalPrecipitation': 0.3,
  'windDirection': 253,
  'windGust': 14,
  'windSpeed': 6},
 {'airTemperature': 16,
  'cloudCover': 11,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 16,
  'forecastTimeUtc': '2023-09-02 18:00:00',
  'relativeHumidity': 76,
  'seaLevelPressure': 1017,
  'totalPrecipitation': 0,
  'windDirection': 252,
  'windGust': 10,
  'windSpeed': 4},
 {'airTemperature': 14.6,
  'cloudCover': 10,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 14.6,
  'forecastTimeUtc': '2023-09-02 21:00:00',
  'relativeHumidity': 83,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 254,
  'windGust': 8,
  'windSpeed': 5},
 {'airTemperature': 13.4,
  'cloudCover': 14,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 13.4,
  'forecastTimeUtc': '2023-09-03 00:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 255,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 12.6,
  'cloudCover': 17,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 12.6,
  'forecastTimeUtc': '2023-09-03 03:00:00',
  'relativeHumidity': 97,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 254,
  'windGust': 8,
  'windSpeed': 3},
 {'airTemperature': 14.6,
  'cloudCover': 94,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 14.6,
  'forecastTimeUtc': '2023-09-03 06:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1019,
  'totalPrecipitation': 0,
  'windDirection': 254,
  'windGust': 9,
  'windSpeed': 5},]
l6 = [
 {'airTemperature': 17.8,
  'cloudCover': 45,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 17.8,
  'forecastTimeUtc': '2023-09-03 09:00:00',
  'relativeHumidity': 75,
  'seaLevelPressure': 1019,
  'totalPrecipitation': 0.3,
  'windDirection': 255,
  'windGust': 10,
  'windSpeed': 4},
 {'airTemperature': 19.6,
  'cloudCover': 52,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 19.6,
  'forecastTimeUtc': '2023-09-03 12:00:00',
  'relativeHumidity': 66,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0.1,
  'windDirection': 253,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 18.5,
  'cloudCover': 86,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 18.5,
  'forecastTimeUtc': '2023-09-03 15:00:00',
  'relativeHumidity': 68,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0.4,
  'windDirection': 248,
  'windGust': 8,
  'windSpeed': 3},
 {'airTemperature': 14.3,
  'cloudCover': 23,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 14.3,
  'forecastTimeUtc': '2023-09-03 18:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 230,
  'windGust': 6,
  'windSpeed': 2},
 {'airTemperature': 12.4,
  'cloudCover': 28,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': 12.4,
  'forecastTimeUtc': '2023-09-03 21:00:00',
  'relativeHumidity': 97,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 237,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': 11.4,
  'cloudCover': 81,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 11.4,
  'forecastTimeUtc': '2023-09-04 00:00:00',
  'relativeHumidity': 97,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 271,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': 13.1,
  'cloudCover': 59,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 13.1,
  'forecastTimeUtc': '2023-09-04 06:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1018,
  'totalPrecipitation': 0,
  'windDirection': 344,
  'windGust': 3,
  'windSpeed': 1},]
l7 = [
 {'airTemperature': 18.8,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 18.8,
  'forecastTimeUtc': '2023-09-04 12:00:00',
  'relativeHumidity': 59,
  'seaLevelPressure': 1017,
  'totalPrecipitation': 0.3,
  'windDirection': 352,
  'windGust': 4,
  'windSpeed': 1},
 {'airTemperature': 15.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 15.2,
  'forecastTimeUtc': '2023-09-04 18:00:00',
  'relativeHumidity': 69,
  'seaLevelPressure': 1016,
  'totalPrecipitation': 0,
  'windDirection': 340,
  'windGust': 4,
  'windSpeed': 3},
 {'airTemperature': 11.8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 11.8,
  'forecastTimeUtc': '2023-09-05 00:00:00',
  'relativeHumidity': 82,
  'seaLevelPressure': 1016,
  'totalPrecipitation': 0,
  'windDirection': 314,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 13,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 13,
  'forecastTimeUtc': '2023-09-05 06:00:00',
  'relativeHumidity': 90,
  'seaLevelPressure': 1016,
  'totalPrecipitation': 0,
  'windDirection': 308,
  'windGust': 6,
  'windSpeed': 3}]

# print (len(l))
print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))
print(len(l5))
print(len(l6))
print(len(l7))