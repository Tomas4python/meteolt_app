# Module used for manual review of data, when length of data received differs from standard

l1 =[{'airTemperature': 1.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -0.2,
  'forecastTimeUtc': '2023-10-28 07:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 997,
  'totalPrecipitation': 0,
  'windDirection': 346,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 1.7,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.5,
  'forecastTimeUtc': '2023-10-28 08:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 998,
  'totalPrecipitation': 0,
  'windDirection': 335,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 1.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.7,
  'forecastTimeUtc': '2023-10-28 09:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 998,
  'totalPrecipitation': 0,
  'windDirection': 332,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 1.3,
  'cloudCover': 100,
  'conditionCode': 'light-sleet',
  'feelsLikeTemperature': -1.9,
  'forecastTimeUtc': '2023-10-28 10:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 999,
  'totalPrecipitation': 0.1,
  'windDirection': 335,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 1.2,
  'cloudCover': 100,
  'conditionCode': 'light-sleet',
  'feelsLikeTemperature': -2.1,
  'forecastTimeUtc': '2023-10-28 11:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1000,
  'totalPrecipitation': 0.2,
  'windDirection': 319,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 1.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.1,
  'forecastTimeUtc': '2023-10-28 12:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1001,
  'totalPrecipitation': 0,
  'windDirection': 316,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 1.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.1,
  'forecastTimeUtc': '2023-10-28 13:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1001,
  'totalPrecipitation': 0,
  'windDirection': 319,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 1.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.9,
  'forecastTimeUtc': '2023-10-28 14:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0,
  'windDirection': 309,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 1.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.1,
  'forecastTimeUtc': '2023-10-28 15:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1003,
  'totalPrecipitation': 0,
  'windDirection': 301,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 1.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.1,
  'forecastTimeUtc': '2023-10-28 16:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 302,
  'windGust': 6,
  'windSpeed': 2},
 {'airTemperature': 0.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.4,
  'forecastTimeUtc': '2023-10-28 17:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 292,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 0.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.4,
  'forecastTimeUtc': '2023-10-28 18:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 290,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 0.8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.5,
  'forecastTimeUtc': '2023-10-28 19:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 294,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 0.6,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.8,
  'forecastTimeUtc': '2023-10-28 20:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 302,
  'windGust': 5,
  'windSpeed': 3},
 {'airTemperature': 0.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.9,
  'forecastTimeUtc': '2023-10-28 21:00:00',
  'relativeHumidity': 87,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 291,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 0.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.9,
  'forecastTimeUtc': '2023-10-28 22:00:00',
  'relativeHumidity': 87,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 289,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': 0.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.9,
  'forecastTimeUtc': '2023-10-28 23:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 279,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': -0.1,
  'cloudCover': 96,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -2.6,
  'forecastTimeUtc': '2023-10-29 00:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 294,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': -0.7,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': -3.3,
  'forecastTimeUtc': '2023-10-29 01:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 285,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': -1.2,
  'cloudCover': 78,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -3.9,
  'forecastTimeUtc': '2023-10-29 02:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 318,
  'windGust': 3,
  'windSpeed': 2},
 {'airTemperature': -1.5,
  'cloudCover': 47,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': -1.5,
  'forecastTimeUtc': '2023-10-29 03:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 328,
  'windGust': 3,
  'windSpeed': 1},
 {'airTemperature': -1.8,
  'cloudCover': 80,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.8,
  'forecastTimeUtc': '2023-10-29 04:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 340,
  'windGust': 2,
  'windSpeed': 1},
 {'airTemperature': -1.3,
  'cloudCover': 36,
  'conditionCode': 'partly-cloudy',
  'feelsLikeTemperature': -1.3,
  'forecastTimeUtc': '2023-10-29 05:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1012,
  'totalPrecipitation': 0,
  'windDirection': 100,
  'windGust': 1,
  'windSpeed': 0},
 {'airTemperature': -1.1,
  'cloudCover': 16,
  'conditionCode': 'clear',
  'feelsLikeTemperature': -1.1,
  'forecastTimeUtc': '2023-10-29 06:00:00',
  'relativeHumidity': 88,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0,
  'windDirection': 184,
  'windGust': 1,
  'windSpeed': 1},]
l2 = [
 {'airTemperature': 0.1,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 0.1,
  'forecastTimeUtc': '2023-10-29 07:00:00',
  'relativeHumidity': 81,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0,
  'windDirection': 194,
  'windGust': 2,
  'windSpeed': 1},
 {'airTemperature': 1.1,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 1.1,
  'forecastTimeUtc': '2023-10-29 08:00:00',
  'relativeHumidity': 76,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 184,
  'windGust': 3,
  'windSpeed': 1},
 {'airTemperature': 2,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 2,
  'forecastTimeUtc': '2023-10-29 09:00:00',
  'relativeHumidity': 73,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 172,
  'windGust': 3,
  'windSpeed': 1},
 {'airTemperature': 2.8,
  'cloudCover': 16,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 0.8,
  'forecastTimeUtc': '2023-10-29 10:00:00',
  'relativeHumidity': 70,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 156,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 3.7,
  'cloudCover': 68,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 1.8,
  'forecastTimeUtc': '2023-10-29 11:00:00',
  'relativeHumidity': 67,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 172,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 4,
  'cloudCover': 92,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 2.2,
  'forecastTimeUtc': '2023-10-29 12:00:00',
  'relativeHumidity': 67,
  'seaLevelPressure': 1014,
  'totalPrecipitation': 0,
  'windDirection': 167,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 4,
  'cloudCover': 53,
  'conditionCode': 'cloudy-with-sunny-intervals',
  'feelsLikeTemperature': 1.3,
  'forecastTimeUtc': '2023-10-29 13:00:00',
  'relativeHumidity': 66,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0,
  'windDirection': 153,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 3.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.7,
  'forecastTimeUtc': '2023-10-29 14:00:00',
  'relativeHumidity': 71,
  'seaLevelPressure': 1013,
  'totalPrecipitation': 0,
  'windDirection': 140,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 2.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -0.6,
  'forecastTimeUtc': '2023-10-29 15:00:00',
  'relativeHumidity': 76,
  'seaLevelPressure': 1012,
  'totalPrecipitation': 0,
  'windDirection': 143,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 2.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.6,
  'forecastTimeUtc': '2023-10-29 16:00:00',
  'relativeHumidity': 80,
  'seaLevelPressure': 1012,
  'totalPrecipitation': 0,
  'windDirection': 142,
  'windGust': 7,
  'windSpeed': 4},
 {'airTemperature': 2.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': -1.6,
  'forecastTimeUtc': '2023-10-29 17:00:00',
  'relativeHumidity': 84,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 150,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 2.2,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': -2.2,
  'forecastTimeUtc': '2023-10-29 18:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0.6,
  'windDirection': 154,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 2.7,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': -1.5,
  'forecastTimeUtc': '2023-10-29 19:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0.4,
  'windDirection': 163,
  'windGust': 11,
  'windSpeed': 5},
 {'airTemperature': 3.6,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': -0.9,
  'forecastTimeUtc': '2023-10-29 20:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0.2,
  'windDirection': 175,
  'windGust': 11,
  'windSpeed': 6},
 {'airTemperature': 4.6,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.4,
  'forecastTimeUtc': '2023-10-29 21:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 184,
  'windGust': 12,
  'windSpeed': 6},
 {'airTemperature': 5.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 5.5,
  'forecastTimeUtc': '2023-10-29 22:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1008,
  'totalPrecipitation': 0,
  'windDirection': 185,
  'windGust': 12,
  'windSpeed': 6},
 {'airTemperature': 6.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 6.3,
  'forecastTimeUtc': '2023-10-29 23:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 187,
  'windGust': 11,
  'windSpeed': 6},
 {'airTemperature': 7,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 7,
  'forecastTimeUtc': '2023-10-30 00:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 194,
  'windGust': 11,
  'windSpeed': 6},
 {'airTemperature': 7.7,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 7.7,
  'forecastTimeUtc': '2023-10-30 01:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0.2,
  'windDirection': 185,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8,
  'forecastTimeUtc': '2023-10-30 02:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 202,
  'windGust': 10,
  'windSpeed': 4},
 {'airTemperature': 8.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.2,
  'forecastTimeUtc': '2023-10-30 03:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 201,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 8.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.3,
  'forecastTimeUtc': '2023-10-30 04:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 195,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 8.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.4,
  'forecastTimeUtc': '2023-10-30 05:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 192,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 8.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.4,
  'forecastTimeUtc': '2023-10-30 06:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 192,
  'windGust': 8,
  'windSpeed': 4},]
l3 = [
 {'airTemperature': 8.6,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.6,
  'forecastTimeUtc': '2023-10-30 07:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 192,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 9.1,
  'cloudCover': 97,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 9.1,
  'forecastTimeUtc': '2023-10-30 08:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 200,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 10.6,
  'cloudCover': 4,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 10.6,
  'forecastTimeUtc': '2023-10-30 09:00:00',
  'relativeHumidity': 92,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 211,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 12.2,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 12.2,
  'forecastTimeUtc': '2023-10-30 10:00:00',
  'relativeHumidity': 89,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 225,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 13.3,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 13.3,
  'forecastTimeUtc': '2023-10-30 11:00:00',
  'relativeHumidity': 86,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 226,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 13.7,
  'cloudCover': 0,
  'conditionCode': 'clear',
  'feelsLikeTemperature': 13.7,
  'forecastTimeUtc': '2023-10-30 12:00:00',
  'relativeHumidity': 85,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 224,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 11.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 11.1,
  'forecastTimeUtc': '2023-10-30 15:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 210,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 10.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 10.2,
  'forecastTimeUtc': '2023-10-30 18:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 209,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 10.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 10.2,
  'forecastTimeUtc': '2023-10-30 21:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 209,
  'windGust': 6,
  'windSpeed': 4},
 {'airTemperature': 9.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 9.1,
  'forecastTimeUtc': '2023-10-31 00:00:00',
  'relativeHumidity': 98,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0,
  'windDirection': 205,
  'windGust': 5,
  'windSpeed': 2},
 {'airTemperature': 8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8,
  'forecastTimeUtc': '2023-10-31 03:00:00',
  'relativeHumidity': 99,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 177,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 8.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8.3,
  'forecastTimeUtc': '2023-10-31 06:00:00',
  'relativeHumidity': 100,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 161,
  'windGust': 5,
  'windSpeed': 3},]
l4 = [
 {'airTemperature': 11.3,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 11.3,
  'forecastTimeUtc': '2023-10-31 09:00:00',
  'relativeHumidity': 96,
  'seaLevelPressure': 1005,
  'totalPrecipitation': 0,
  'windDirection': 150,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 12.3,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 12.3,
  'forecastTimeUtc': '2023-10-31 12:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0.7,
  'windDirection': 139,
  'windGust': 7,
  'windSpeed': 3},
 {'airTemperature': 11.9,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 11.9,
  'forecastTimeUtc': '2023-10-31 15:00:00',
  'relativeHumidity': 94,
  'seaLevelPressure': 1000,
  'totalPrecipitation': 3.4,
  'windDirection': 148,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 12.4,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 12.4,
  'forecastTimeUtc': '2023-10-31 18:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 999,
  'totalPrecipitation': 2.4,
  'windDirection': 199,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 12.6,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 12.6,
  'forecastTimeUtc': '2023-10-31 21:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 999,
  'totalPrecipitation': 0.3,
  'windDirection': 204,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 12,
  'cloudCover': 100,
  'conditionCode': 'rain',
  'feelsLikeTemperature': 12,
  'forecastTimeUtc': '2023-11-01 00:00:00',
  'relativeHumidity': 97,
  'seaLevelPressure': 998,
  'totalPrecipitation': 0.6,
  'windDirection': 209,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 11.2,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 11.2,
  'forecastTimeUtc': '2023-11-01 03:00:00',
  'relativeHumidity': 99,
  'seaLevelPressure': 999,
  'totalPrecipitation': 0.1,
  'windDirection': 248,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 9.8,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 9.8,
  'forecastTimeUtc': '2023-11-01 06:00:00',
  'relativeHumidity': 98,
  'seaLevelPressure': 1000,
  'totalPrecipitation': 0.2,
  'windDirection': 261,
  'windGust': 8,
  'windSpeed': 5},]
l5 = [
 {'airTemperature': 9.7,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 9.7,
  'forecastTimeUtc': '2023-11-01 09:00:00',
  'relativeHumidity': 95,
  'seaLevelPressure': 1001,
  'totalPrecipitation': 0.2,
  'windDirection': 296,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 9.5,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 9.5,
  'forecastTimeUtc': '2023-11-01 12:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0.2,
  'windDirection': 323,
  'windGust': 8,
  'windSpeed': 4},
 {'airTemperature': 7.6,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 7.6,
  'forecastTimeUtc': '2023-11-01 15:00:00',
  'relativeHumidity': 91,
  'seaLevelPressure': 1004,
  'totalPrecipitation': 0,
  'windDirection': 338,
  'windGust': 9,
  'windSpeed': 5},
 {'airTemperature': 5.8,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 5.8,
  'forecastTimeUtc': '2023-11-01 18:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0.5,
  'windDirection': 341,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 4.8,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 1.1,
  'forecastTimeUtc': '2023-11-01 21:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1007,
  'totalPrecipitation': 0.2,
  'windDirection': 336,
  'windGust': 10,
  'windSpeed': 5},
 {'airTemperature': 4.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.7,
  'forecastTimeUtc': '2023-11-02 00:00:00',
  'relativeHumidity': 93,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 329,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 3.8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.4,
  'forecastTimeUtc': '2023-11-02 03:00:00',
  'relativeHumidity': 90,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 325,
  'windGust': 9,
  'windSpeed': 4},
 {'airTemperature': 3.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.3,
  'forecastTimeUtc': '2023-11-02 06:00:00',
  'relativeHumidity': 90,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 317,
  'windGust': 7,
  'windSpeed': 3},]
l6 = [
 {'airTemperature': 4.7,
  'cloudCover': 92,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 3,
  'forecastTimeUtc': '2023-11-02 09:00:00',
  'relativeHumidity': 84,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 302,
  'windGust': 6,
  'windSpeed': 2},
 {'airTemperature': 5.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 5.4,
  'forecastTimeUtc': '2023-11-02 12:00:00',
  'relativeHumidity': 72,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 306,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 4.9,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 4.9,
  'forecastTimeUtc': '2023-11-02 15:00:00',
  'relativeHumidity': 82,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 103,
  'windGust': 5,
  'windSpeed': 0},
 {'airTemperature': 4.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 2.8,
  'forecastTimeUtc': '2023-11-02 18:00:00',
  'relativeHumidity': 80,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 107,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 4.1,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 2.3,
  'forecastTimeUtc': '2023-11-02 21:00:00',
  'relativeHumidity': 83,
  'seaLevelPressure': 1010,
  'totalPrecipitation': 0,
  'windDirection': 114,
  'windGust': 4,
  'windSpeed': 2},
 {'airTemperature': 4.4,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 1.8,
  'forecastTimeUtc': '2023-11-03 00:00:00',
  'relativeHumidity': 84,
  'seaLevelPressure': 1011,
  'totalPrecipitation': 0,
  'windDirection': 114,
  'windGust': 6,
  'windSpeed': 3},
 {'airTemperature': 4.5,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 0.7,
  'forecastTimeUtc': '2023-11-03 06:00:00',
  'relativeHumidity': 88,
  'seaLevelPressure': 1009,
  'totalPrecipitation': 0,
  'windDirection': 104,
  'windGust': 10,
  'windSpeed': 5},]
l7 = [
 {'airTemperature': 8,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 8,
  'forecastTimeUtc': '2023-11-03 12:00:00',
  'relativeHumidity': 83,
  'seaLevelPressure': 1006,
  'totalPrecipitation': 0,
  'windDirection': 96,
  'windGust': 12,
  'windSpeed': 5},
 {'airTemperature': 9.8,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 9.8,
  'forecastTimeUtc': '2023-11-03 18:00:00',
  'relativeHumidity': 83,
  'seaLevelPressure': 1002,
  'totalPrecipitation': 0.1,
  'windDirection': 139,
  'windGust': 14,
  'windSpeed': 7},
 {'airTemperature': 10.2,
  'cloudCover': 100,
  'conditionCode': 'cloudy',
  'feelsLikeTemperature': 10.2,
  'forecastTimeUtc': '2023-11-04 00:00:00',
  'relativeHumidity': 73,
  'seaLevelPressure': 998,
  'totalPrecipitation': 0,
  'windDirection': 156,
  'windGust': 15,
  'windSpeed': 8},
 {'airTemperature': 10.5,
  'cloudCover': 100,
  'conditionCode': 'light-rain',
  'feelsLikeTemperature': 10.5,
  'forecastTimeUtc': '2023-11-04 06:00:00',
  'relativeHumidity': 73,
  'seaLevelPressure': 995,
  'totalPrecipitation': 0.1,
  'windDirection': 173,
  'windGust': 16,
  'windSpeed': 8}]

# print (len(l))
print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))
print(len(l5))
print(len(l6))
print(len(l7))