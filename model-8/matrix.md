|   CAN-ID  |                     Data                    |                        Description                        |
|:---------:|:-------------------------------------------:|:---------------------------------------------------------:|
|    040    |               0000000001000000              |                      Belt warning on                      |
|    040    |               0000000000000000              |                      Belt warning off                     |
|  101/308  | 0000000000000000 / 0000X_1X_2X_3X_400000000 | Set speed X1 = 0.5kmh X2 = 0.01kmh X3 = 67kmh X4 = 4.1kmh |
|    30D    |               0001000000000000              |                   Parking light (green)                   |
|    30D    |               0400000000000000              |                    Parking light (red)                    |
|    363    |               0000440000000000              |                       Indicator left                      |
|    363    |               0000F80000000000              |                      Indicator right                      |
|    363    |               FFFFFFFFFFFFFFFF              |                  Indicator left and right                 |
|    363    |               000000000000000               |                       Indicators off                      |
|    397    |               0000000000000020              |                    Lane assist (yellow)                   |
|    397    |               0000000000000050              |                    Lane assist (green)                    |
|    3C0    |                   00000200                  |                        Ignition on                        |
|    3C0    |                   00000100                  |                        Ignition off                       |
|    3C0    |                BC204007A5BCB8               |                        Show symbols                       |
|    585    |                00020000000000               |                          Show TR                          |
|    590    |               00000000000D0000              |                        Show "SAFE"                        |
|    590    |               0000000000020000              |                          Show L1                          |
|    590    |               00000000000F0000              |                        Show L1 2/2                        |
|    5F0    |                 222222222222                |                        Dim Display                        |
|  5F0/662  |     FFFFFFFFFFFFFFFF / 00000F0000000000     |                         Brights on                        |
|  5F0/662  |     FFFFFFFFFFFFFFFF / 00000000B0000000     |                    Brights automatic on                   |
|    661    |               0002000000000000              |                       3 green Arrows                      |
|    663    |              0400000X_100000000             |           Show TR in percent Must be send twice           |
| 700 / 714 |               0210030000000000              |                 Start programming session                 |
| 700 / 714 |               0210400000000000              |                   Start extended session                  |
|    714    |             0210X_1X_20000000000            |                 Start proprietary session?                |
|    714    |               0211820000000000              |                           Reset                           |
|    714    |               0722225F84E15D03              |                        Read memory?                       |
