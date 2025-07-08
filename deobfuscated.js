# 反混淆后的代码

```javascript
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>第五题 jsRPC例题练习题</title>
        <meta content="{qqqhDDexFaTvMa0kihgqql4096qqqt1075314760lABpzq!x7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,txt,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipak162H8Wxte9vasdRWdl9qqJ1600407196152lEgWWqqh5XmfHRYf62oKx69ItuerNQRyYMyKX4NamAqqYJYrJJu8N5ghrCsU314Hhjqqqqqqqqqqqq~FD6ABkKTm3axUocqfMumPJmEYE0w.JCZStu2gZnkxQXpp5UsvE.ya4loEwBajBnkmAQ3B_TMoA.YYyC_NFFE7e1kAE5ShZo4b8FSwdbuZVBTxZPk6sIrZN9HAsx7B_mkmKNl7S1kUVBmXgYsv1za.vY6MQeeK2vOHsx2Cd2DmwJSenbdyMwAGd2FkQ5TR41B8UdpTf6u_VENSdKPcKMxf.ccqYFSkZmvus.eu.CdnwyyUOvbDIyaLzc55JMpezc.9hi3TBbOX8iY_NbOfIhxBBDvBJMfeXc.LhiLTPbOFYtyJNmcHUewB9oFaEE0X0oP2hLJtvmnTheYEPntcYFxVflX3QRWGqqVpKy0KoYIQVrnA6Rlw9NZXAOo30eljTuAgmeehhIUrtA;4kUyzUi8kgD7ll6J2MqFBA;qqr1MlK02KnfRx2GPpcmDEllbAcmmtVlqql3650Ddfe167qqr0k443qqr0k117qqq{Ul8GO0PUAtyf0bb1m3gGdOUcW8RYSanBDtW2O9Kcq8Ep0CUtRQNm0bPkrEZ0.96cE8xfuwoTuHDJPQ0pf3oR4FUa">
        <script type="text/javascript" charset="iso-8859-1" src="/static/match/safety/match10/rs.js" r='m'></script>
        <script type="text/javascript" charset="iso-8859-1" src="/challenge/5/rsnkw2ksph" r='y'></script>
        <script type="text/javascript" r="m">
            (function() {
                var counter = 0;
                var controlFlowData = [
                    [7, 0, 10, 8, 2, 5, 1, 6, 4, 9, 3],
                    [33, 84, 16, 31, 39, 98, 45, 26, 47, 26, 12, 49, 4, 85, 86, 18, 59, 23, 56, 89, 36, 30, 94, 42, 78, 41, 72, 51, 26, 57, 63, 69, 62, 88, 65, 8, 96, 81, 93, 70, 8, 25, 46, 58, 26, 50, 60, 8, 61, 92, 13, 31, 76, 8, 83, 53, 38, 37, 28, 7, 68, 82, 8, 22, 75, 8, 67, 20, 52, 34, 26, 95, 44, 6, 52, 73, 97, 26, 3, 52, 26, 10, 31, 19, 17, 11, 90, 55, 26, 15, 9, 71, 35, 74, 91, 0, 79, 64, 5, 27, 40, 14, 77, 29, 87, 24, 80, 21, 1, 48, 32, 99, 54, 43, 66, 2, 26],
                    [29, 11, 24, 0, 24, 23, 20, 7, 1, 15, 22, 6, 33, 10, 8, 22, 28, 12, 14, 12, 4, 21, 2, 17, 25, 9, 27, 30, 27, 18, 27, 26, 27, 13, 3, 27, 5, 27, 16, 19, 31, 32, 22],
                    [32, 4, 43, 12, 23, 30, 36, 15, 11, 0, 35, 5, 9, 14, 6, 33, 29, 40, 47, 8, 31, 1, 9, 2, 23, 39, 20, 26, 22, 16, 4, 34, 25, 17, 28, 34, 37, 10, 18, 10, 42, 13, 42, 27, 9, 10, 19, 27, 29, 45, 46, 24, 41, 3, 21, 18, 27, 19, 45, 15, 44, 7, 38, 36],
                    [27, 0, 12, 21, 0, 16, 36, 4, 8, 30, 0, 22, 20, 24, 0, 32, 28, 24, 11, 23, 7, 15, 1, 14, 9, 6, 11, 5, 13, 17, 25, 29, 1, 26, 6, 18, 5, 0, 35, 19, 31, 33, 8, 10, 34, 2, 3]
                ];

                function modulo(value, mod) {
                    return Math.abs(value) % mod;
                }

                function processArray(arr) {
                    arr[modulo(getValue1(arr), 16)] = getValue2(arr);
                    var temp1 = arr[modulo(getValue3(), 16)];
                    var temp1 = getValue4(arr);
                    var temp2 = getValue5(arr);
                    var temp2 = getValue6();
                    arr[modulo(getValue7() - arr[modulo(getValue8(), 16)], 16)] = arr[modulo(getValue9() + getValue10(), 16)];
                    arr[2] = getValue7() - arr[modulo(getValue8(), 16)];
                    updateArray(arr);
                    arr[10] = getValue9() - arr[modulo(getValue11(), 16)];
                    return arr[modulo(getValue7() - arr[modulo(getValue8(), 16)], 16)];
                }

                function getValue1(arr) {
                    arr[4] = getValue12();
                    arr[modulo(getValue7(), 16)] = getValue13();
                    var temp1 = getValue14();
                    var temp2 = getValue15();
                    return getValue6() + getValue16();
                }

                function getValue12() {
                    return 2;
                }

                function getValue7() {
                    return 9;
                }

                function getValue13() {
                    return 15;
                }

                function getValue14() {
                    return 8;
                }

                function getValue15() {
                    return 6;
                }

                function getValue6() {
                    return 13;
                }

                function getValue16() {
                    return 3;
                }

                function getValue2(arr) {
                    if (getValue17()) {
                        arr[modulo(getValue14(), 16)] = getValue15();
                    }
                    arr[0] = getValue18();
                    var temp2 = getValue12();
                    if (getValue17()) {
                        arr[11] = getValue9();
                    }
                    arr[14] = getValue8();
                    updateArray2(arr);
                    return getValue19(arr);
                }

                function getValue17() {
                    return 5;
                }

                function getValue18() {
                    return 14;
                }

                function getValue9() {
                    return 1;
                }

                function getValue3() {
                    return 0;
                }

                function getValue8() {
                    return 12;
                }

                function updateArray2(arr) {
                    var temp2 = getValue10();
                    var temp2 = getValue6();
                    var temp2 = getValue7();
                    arr[modulo(getValue8(), 16)] = getValue20();
                    return getValue14();
                }

                function getValue10() {
                    return 7;
                }

                function getValue20() {
                    return 10;
                }

                function getValue19(arr) {
                    arr[modulo(getValue6(), 16)] = getValue16();
                    arr[9] = getValue13();
                    arr[modulo(getValue20(), 16)] = getValue14();
                    return getValue15();
                }

                function getValue4(arr) {
                    arr[modulo(getValue17(), 16)] = getValue21();
                    arr[1] = getValue10();
                    updateArray3(arr);
                    updateArray4(arr);
                    return getValue17();
                }

                function getValue21() {
                    return 11;
                }

                function updateArray3(arr) {
                    arr[3] = getValue7();
                    arr[15] = getValue17();
                    var temp2 = getValue15();
                    var temp1 = getValue11();
                    arr[2] = getValue3();
                    return getValue18();
                }

                function getValue11() {
                    return 4;
                }

                function updateArray4(arr) {
                    arr[modulo(getValue21(), 16)] = getValue9();
                    arr[7] = getValue6();
                    arr[3] = getValue7();
                    return getValue13();
                }

                function getValue5(arr) {
                    var temp1 = getValue16();
                    var temp1 = getValue7();
                    arr[15] = getValue17();
                    arr[11] = getValue9();
                    return getValue10();
                }

                function updateArray(arr) {
                    var temp1 = getValue20();
                    if (checkCondition1(arr)) {
                        arr[3] = getValue7();
                    }
                    var temp2 = getValue8();
                    if (arr[modulo(getValue11(), 16)]) {
                        if (getValue16()) {
                            var temp1 = getValue20();
                        }
                    }
                    updateArray5(arr);
                    arr[6] = getValue6() + getValue16();
                    updateArray6(arr);
                    var temp2 = getValue6();
                    return arr[modulo(getValue7() + getValue13(), 16)];
                }

                function checkCondition1(arr) {
                    arr[modulo(getValue6(), 16)] = getValue16();
                    var temp2 = getValue8();
                    var temp1 = getValue20();
                    arr[modulo(getValue9(), 16)] = getValue10();
                    return getValue6();
                }

                function updateArray5(arr) {
                    var temp2 = getValue14();
                    var temp2 = getValue16();
                    if (getValue13()) {
                        var temp2 = getValue15();
                    }
                    if (getValue8()) {
                        arr[modulo(getValue21(), 16)] = getValue9();
                    }
                    var temp1 = getValue13();
                    var temp1 = getValue17();
                    return arr[modulo(getValue14(), 16)];
                }

                function updateArray6(arr) {
                    arr[12] = getValue20();
                    arr[modulo(getValue9(), 16)] = getValue10();
                    arr[13] = getValue16();
                    arr[modulo(getValue18(), 16)] = getValue8();
                    return updateArray7(arr);
                }

                function updateArray7(arr) {
                    arr[modulo(getValue9(), 16)] = getValue10();
                    arr[modulo(getValue12(), 16)] = getValue3();
                    var temp2 = getValue17();
                    var temp1 = getValue21();
                    return getValue9();
                }

                var windowRef, tsObject, globalWindow, arrayRef, tsData, processFunc, stringRef;
                var isInitialized, currentValue, index = counter, currentFlow = controlFlowData[0];
                
                while (true) {
                    currentValue = currentFlow[index++];
                    if (currentValue < 4) {
                        if (currentValue < 1) {
                            globalWindow = window;
                            stringRef = String;
                            arrayRef = Array;
                        } else if (currentValue < 2) {
                            tsData = globalWindow['$_ts'] = {};
                        } else if (currentValue < 3) {
                            return;
                        } else {
                            index += -6;
                        }
                    } else if (currentValue < 8) {
                        if (currentValue < 5) {
                            index += -5;
                        } else if (currentValue < 6) {
                            if (!isInitialized) {
                                index += 1;
                            }
                        } else if (currentValue < 7) {
                            executeFlow(0);
                        } else {
                            windowRef = [4, 16, 64, 256, 1024, 4096, 16384, 65536];
                        }
                    } else {
                        if (currentValue < 9) {
                            index += 5;
                        } else if (currentValue < 10) {
                            isInitialized = !tsData;
                        } else {
                            tsData = globalWindow['$_ts'];
                        }
                    }
                }

                function executeFlow(flowIndex, targetObj) {
                    function readNextValue() {
                        var charCode = encodedString.charCodeAt(position++);
                        var result;
                        if (charCode < 128) {
                            return charCode;
                        } else if (charCode < 251) {
                            return charCode - 32;
                        } else if (charCode === 251) {
                            return 0;
                        } else if (charCode === 254) {
                            charCode = encodedString.charCodeAt(position++);
                            if (charCode >= 128) {
                                charCode -= 32;
                            }
                            result = encodedString.charCodeAt(position++);
                            if (result >= 128) {
                                result -= 32;
                            }
                            return charCode * 219 + result;
                        } else if (charCode === 255) {
                            charCode = encodedString.charCodeAt(position++);
                            if (charCode >= 128) {
                                charCode -= 32;
                            }
                            result = encodedString.charCodeAt(position++);
                            if (result >= 128) {
                                result -= 32;
                            }
                            charCode = charCode * 219 * 219 + result * 219;
                            result = encodedString.charCodeAt(position++);
                            if (result >= 128) {
                                result -= 32;
                            }
                            return charCode + result;
                        } else if (charCode === 252) {
                            result = encodedString.charCodeAt(position++);
                            if (result >= 128) {
                                result -= 32;
                            }
                            return -result;
                        } else if (charCode === 253) {
                            charCode = encodedString.charCodeAt(position++);
                            if (charCode >= 128) {
                                charCode -= 32;
                            }
                            result = encodedString.charCodeAt(position++);
                            if (result >= 128) {
                                result -= 32;
                            }
                            return charCode * -219 - result;
                        }
                    }

                    var position, encodedString, decodedData, value1, stringValue, resultValue, counterValue, indexValue, isInitializedValue, flowValue, currentValue, flowIndexRef, dataArray, tempValue, loopIndex, tempVar1, tempVar2, tempVar3, tempVar4;
                    var value2, value3, getValueFunc = flowIndex, currentFlowRef = controlFlowData[1];
                    
                    while (true) {
                        value3 = currentFlowRef[flowIndexRef++];
                        if (value3 <