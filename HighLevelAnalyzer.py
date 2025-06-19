# MDB Protocol Decoder - 2 BYTE SUPPORT - Enhanced
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame

class Hla(HighLevelAnalyzer):
    result_types = {
        'mdb_cmd': {
            'format': 'CMD: 0x{data.hex_val} ({data.name})'
        },
        'mdb_data': {
            'format': 'DATA: 0x{data.hex_val}'
        },
        'begin_session': {
            'format': 'BEGIN SESSION - Funds: {data.funds}, Level: {data.level}'
        },
        'peripheral_id': {
            'format': 'PERIPHERAL ID - Mfg: {data.mfg}, SN: {data.serial}'
        },
        'vend_approved': {
            'format': 'VEND APPROVED - Amount: {data.amount}'
        },
        'vend_denied': {
            'format': 'VEND DENIED'
        },
        'reader_config': {
            'format': 'READER CONFIG - Level: {data.level}, Country: {data.country}'
        },
        'ack_response': {
            'format': 'ACK'
        },
        'poll_command': {
            'format': 'POLL'
        },
    }
    def __init__(self):
        self.BironcekiKomut = 0x00
        
        # ByTaymur MDB Decoder v9 startup
        print("=" * 65)
        print("🚀 ByTaymur MDB Protocol Decoder v9 - Started!")
        print("📧 GitHub: https://github.com/ByTaymur")
        print("🎯 Purpose: Detailing MDB commands and parsing data")
        print("⚡ Feature: 9-bit → 2 byte decode system")
        print("💡 Logic: Each packet analyzed by length & content")
        print("")
        print("📖 Symbol Guide:")
        print("   -> = ACK Response (Device acknowledges)")
        print("   <- = POLL Command (VMC polls device)")
        print("=" * 65)
    
    def decode(self, frame: AnalyzerFrame):
        if frame.type != 'data':
            return None
            
        DataBytes = frame.data['data']
        
        # Debug için önce yazdır
        if len(DataBytes) >= 2:
            # DataBytes[0]==0x01 koşullu kontroller
            if DataBytes[0] == 0x01 and DataBytes[1] == 0x00:
                print("->")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x01:
                print(f"READER_CONFIG_DATA bytes: {DataBytes.hex()} (len: {len(DataBytes)})")    
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x02:
                print(f"DISPLAY_REQUEST bytes: {DataBytes.hex()} (len: {len(DataBytes)})")    
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x03:
                print(f"BEGIN_SESSION bytes: {DataBytes.hex()} (len: {len(DataBytes)})")    
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x04:
                print(f"SESSION_CANCEL bytes: {DataBytes.hex()} (len: {len(DataBytes)})")    
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x05:
                print(f"VEND_APPROVED bytes: {DataBytes.hex()} (len: {len(DataBytes)})")    
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x06:
                print(f"VEND_DENIED bytes: {DataBytes.hex()} (len: {len(DataBytes)})")                 
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x07:
                print(f"END_SESSION bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x08:
                print(f"CANCEL_REQUEST bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x09:
                print(f"PERIPHERAL_ID bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0A:
                print(f"MALFUNCTION bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0B:
                print(f"STATUS bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0C:
                print(f"RESET bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0D:
                print(f"SETUP_CONFIG_DATA bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0E:
                print(f"POLL bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x0F:
                print(f"TYPE_PAYOUT bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            elif DataBytes[0] == 0x00 and DataBytes[1] == 0x10:
                print(f"DISPENSE bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
            
            # Diğer genel kontroller
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x10:
                print(f"RESET bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x10
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x11:
                print(f"SETUP bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x11
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x12:
                print("<-")
                self.BironcekiKomut = 0x12
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x13:
                print(f"VEND bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x13 
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x14:
                print(f"READER bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x14  
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x15:
                print(f"REVALUE bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x15
            elif DataBytes[0] == 0x01 and DataBytes[1] == 0x17:
                print(f"EXPANSION bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
                self.BironcekiKomut = 0x17
            else:
                if self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x12:
                    pass  # ACK response, normal
                elif self.BironcekiKomut == 0x11 and DataBytes[0] == 0x00 and DataBytes[1] == 0x01:
                    if len(DataBytes) >= 16:  # Full READER_CONFIG_DATA (8 byte * 2 = 16)
                        print(f"SETUP->READER_CONFIG response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Feature Level: {DataBytes[2]}, Country: {DataBytes[4]:02X}{DataBytes[6]:02X}")
                        print(f"  Scale Factor: {DataBytes[8]}, Decimal Places: {DataBytes[10]}")
                        
                        # Enhanced AnalyzerFrame döndür
                        return AnalyzerFrame('reader_config', frame.start_time, frame.end_time, {
                            'level': DataBytes[2],
                            'country': f'0x{(DataBytes[4] << 8) | DataBytes[6]:04X}'
                        })
                    else:
                        print(f"SETUP->READER_CONFIG response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x01:
                    if len(DataBytes) >= 16:  # Full READER_CONFIG_DATA 
                        print(f"POLL->READER_CONFIG response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                        # Enhanced AnalyzerFrame döndür
                        return AnalyzerFrame('reader_config', frame.start_time, frame.end_time, {
                            'level': DataBytes[2],
                            'country': f'0x{(DataBytes[4] << 8) | DataBytes[6]:04X}'
                        })
                    else:
                        print(f"POLL->READER_CONFIG response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x02:
                    if len(DataBytes) >= 6:  # DISPLAY_REQUEST minimum
                        DisplayTime = DataBytes[2] if len(DataBytes) > 2 else 0
                        DisplayDataLen = (len(DataBytes) - 4) // 2  # Remaining bytes for display data
                        print(f"POLL->DISPLAY_REQUEST response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Display Time: {DisplayTime * 0.1}s, Data Length: {DisplayDataLen}")
                    else:
                        print(f"POLL->DISPLAY_REQUEST response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x03:
                    if len(DataBytes) >= 6:  # BEGIN_SESSION Level 01 minimum
                        FundsAvailable = (DataBytes[2] << 8) | DataBytes[4] if len(DataBytes) >= 6 else 0
                        print(f"POLL->BEGIN_SESSION response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        Level = 1
                        if len(DataBytes) == 6:  # Level 01
                            print(f"  Level 01 - Funds: {FundsAvailable}")
                        elif len(DataBytes) >= 20:  # Level 02 (10 byte * 2 = 20)
                            Level = 2
                            MediaID = f"{DataBytes[6]:02X}{DataBytes[8]:02X}{DataBytes[10]:02X}{DataBytes[12]:02X}"
                            PaymentType = DataBytes[14]
                            print(f"  Level 02 - Funds: {FundsAvailable}, Media ID: {MediaID}, Type: {PaymentType:02X}")
                        elif len(DataBytes) >= 34:  # Level 03 expanded (17 byte * 2 = 34)
                            Level = 3
                            print(f"  Level 03 - Extended BEGIN_SESSION")
                            
                        # Enhanced AnalyzerFrame döndür
                        return AnalyzerFrame('begin_session', frame.start_time, frame.end_time, {
                            'funds': FundsAvailable,
                            'level': Level
                        })
                    else:
                        print(f"POLL->BEGIN_SESSION response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x09:
                    if len(DataBytes) >= 58:  # PERIPHERAL_ID Level 01/02 (29 byte * 2 = 58)
                        try:
                            ManufCode = f"{chr(DataBytes[2])}{chr(DataBytes[4])}{chr(DataBytes[6])}"
                            SerialStart = DataBytes[8:20:2]  # Every other byte for serial
                            SerialStr = ''.join([chr(b) for b in SerialStart if b != 0])
                            print(f"POLL->PERIPHERAL_ID response: {DataBytes.hex()} (len: {len(DataBytes)})")
                            print(f"  Manufacturer: {ManufCode}")
                            if len(DataBytes) >= 66:  # Level 03 (33 byte * 2 = 66)
                                print(f"  Level 03 with Optional Features")
                                
                            # Enhanced AnalyzerFrame döndür
                            return AnalyzerFrame('peripheral_id', frame.start_time, frame.end_time, {
                                'mfg': ManufCode,
                                'serial': SerialStr[:8]
                            })
                        except:
                            print(f"POLL->PERIPHERAL_ID response (parse error): {DataBytes.hex()} (len: {len(DataBytes)})")
                    else:
                        print(f"POLL->PERIPHERAL_ID response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x14:
                    if len(DataBytes) >= 24:  # SELECTION_REQUEST minimum (12 byte * 2 = 24)
                        FundsAvailable = (DataBytes[2] << 8) | DataBytes[4]
                        MediaID = f"{DataBytes[6]:02X}{DataBytes[8]:02X}{DataBytes[10]:02X}{DataBytes[12]:02X}"
                        ItemNumber = (DataBytes[20] << 8) | DataBytes[22] if len(DataBytes) >= 24 else 0
                        print(f"POLL->SELECTION_REQUEST response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Funds: {FundsAvailable}, Item: {ItemNumber}, Media ID: {MediaID}")
                        if len(DataBytes) >= 46:  # Expanded mode (23 byte * 2 = 46)
                            print(f"  Expanded SELECTION_REQUEST")
                    else:
                        print(f"POLL->SELECTION_REQUEST response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x00 and DataBytes[1] == 0x05:
                    if len(DataBytes) >= 6:  # VEND_APPROVED minimum
                        VendAmount = (DataBytes[2] << 8) | DataBytes[4]
                        print(f"VEND->VEND_APPROVED response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Vend Amount: {VendAmount}")
                        if len(DataBytes) >= 10:  # Basket mode with options amount
                            OptionsAmount = (DataBytes[6] << 8) | DataBytes[8]
                            print(f"  Options Amount: {OptionsAmount}")
                            
                        # Enhanced AnalyzerFrame döndür
                        return AnalyzerFrame('vend_approved', frame.start_time, frame.end_time, {
                            'amount': VendAmount
                        })
                    else:
                        print(f"VEND->VEND_APPROVED response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x00 and DataBytes[1] == 0x03:
                    # BEGIN_SESSION after VEND REQUEST (Ask Begin Session feature)
                    if len(DataBytes) >= 6:
                        FundsAvailable = (DataBytes[2] << 8) | DataBytes[4]
                        print(f"VEND->BEGIN_SESSION response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Ask Begin Session sequence activated - Funds: {FundsAvailable}")
                        
                        # Enhanced AnalyzerFrame döndür
                        return AnalyzerFrame('begin_session', frame.start_time, frame.end_time, {
                            'funds': FundsAvailable,
                            'level': 1
                        })
                    else:
                        print(f"VEND->BEGIN_SESSION response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x00 and DataBytes[1] == 0x06:
                    print(f"VEND->VEND_DENIED response: {DataBytes.hex()} (len: {len(DataBytes)})")
                    
                    # Enhanced AnalyzerFrame döndür
                    return AnalyzerFrame('vend_denied', frame.start_time, frame.end_time, {})
                    
                elif self.BironcekiKomut == 0x14 and DataBytes[0] == 0x00 and DataBytes[1] == 0x08:
                    print(f"READER->CANCELLED response: {DataBytes.hex()} (len: {len(DataBytes)})")
                    
                elif self.BironcekiKomut == 0x15 and DataBytes[0] == 0x00 and DataBytes[1] == 0x0D:
                    print(f"REVALUE->REVALUE_APPROVED response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x15 and DataBytes[0] == 0x00 and DataBytes[1] == 0x0E:
                    print(f"REVALUE->REVALUE_DENIED response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x15 and DataBytes[0] == 0x00 and DataBytes[1] == 0x0F:
                    if len(DataBytes) >= 6:  # REVALUE_LIMIT_AMOUNT
                        LimitAmount = (DataBytes[2] << 8) | DataBytes[4]
                        print(f"REVALUE->REVALUE_LIMIT response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Limit Amount: {LimitAmount}")
                    else:
                        print(f"REVALUE->REVALUE_LIMIT response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x09:
                    # EXPANSION->PERIPHERAL_ID same as POLL->PERIPHERAL_ID
                    if len(DataBytes) >= 58:
                        try:
                            ManufCode = f"{chr(DataBytes[2])}{chr(DataBytes[4])}{chr(DataBytes[6])}"
                            SerialStart = DataBytes[8:20:2]
                            SerialStr = ''.join([chr(b) for b in SerialStart if b != 0])
                            print(f"EXPANSION->PERIPHERAL_ID response: {DataBytes.hex()} (len: {len(DataBytes)})")
                            print(f"  Manufacturer: {ManufCode}")
                            
                            # Enhanced AnalyzerFrame döndür
                            return AnalyzerFrame('peripheral_id', frame.start_time, frame.end_time, {
                                'mfg': ManufCode,
                                'serial': SerialStr[:8]
                            })
                        except:
                            print(f"EXPANSION->PERIPHERAL_ID response (parse error): {DataBytes.hex()} (len: {len(DataBytes)})")
                    else:
                        print(f"EXPANSION->PERIPHERAL_ID response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x10:
                    if len(DataBytes) >= 6:  # USER_FILE_DATA minimum
                        FileNumber = DataBytes[2]
                        FileLength = DataBytes[4]
                        print(f"EXPANSION->USER_FILE_DATA response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  File Number: {FileNumber}, Length: {FileLength}")
                    else:
                        print(f"EXPANSION->USER_FILE_DATA response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                        
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x11:
                    print(f"EXPANSION->TIME_DATE_REQUEST response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x1B:
                    print(f"EXPANSION->FTL_REQ_TO_RCV response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x1C:
                    print(f"EXPANSION->FTL_RETRY_DENY response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x1D:
                    if len(DataBytes) >= 6:  # FTL_SEND_BLOCK minimum
                        DestAddr = DataBytes[2]
                        BlockNum = DataBytes[4]
                        DataLength = (len(DataBytes) - 6) // 2
                        print(f"EXPANSION->FTL_SEND_BLOCK response: {DataBytes.hex()} (len: {len(DataBytes)})")
                        print(f"  Dest: {DestAddr:02X}, Block: {BlockNum}, Data Length: {DataLength}")
                    else:
                        print(f"EXPANSION->FTL_SEND_BLOCK response (partial): {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x1E:
                    print(f"EXPANSION->FTL_OK_TO_SEND response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0x1F:
                    print(f"EXPANSION->FTL_REQ_TO_SEND response: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x17 and DataBytes[0] == 0x00 and DataBytes[1] == 0xFF:
                    print(f"EXPANSION->DIAGNOSTICS response: {DataBytes.hex()} (len: {len(DataBytes)})")
                
                # VMC Commands için özel durumlar
                elif self.BironcekiKomut == 0x11 and DataBytes[0] == 0x00 and DataBytes[1] == 0x15:
                    print(f"SETUP->SETUP_MAX_MIN_PRICES data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x00 and DataBytes[1] == 0x00:
                    print(f"VEND->VEND_REQUEST data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x00 and DataBytes[1] == 0x37:
                    print(f"VEND->ITEM_PRICE data: {DataBytes.hex()} (len: {len(DataBytes)})")
                    # Basit para hesaplama - sadece hex değerini decimal yap
                    HexValue = DataBytes[1]  # İkinci byte
                    if HexValue > 0:  # 0 değilse decimal göster
                        print(f"  Decimal değer: {HexValue}")
                elif self.BironcekiKomut == 0x13 and DataBytes[0] == 0x01 and DataBytes[1] == 0x3C:
                    print(f"VEND->ITEM_NUMBER data: {DataBytes.hex()} (len: {len(DataBytes)})")
                
                # POLL sonrası gelen data paketleri
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x00:
                    print(f"POLL->ACK data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x15:
                    print(f"POLL->DATA continuation: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x4B:
                    print(f"POLL->CONFIG data: {DataBytes.hex()} (len: {len(DataBytes)})")
                    # bir sonraki ile beraber toplanmasi gerekiyor ki toplam fiyat çiksin 
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x00 and DataBytes[1] == 0x37:
                    print(f"POLL->PRICE data: {DataBytes.hex()} (len: {len(DataBytes)})")
                    # Basit para hesaplama - sadece hex değerini decimal yap
                    HexValue = DataBytes[1]  # İkinci byte
                    if HexValue > 0:  # 0 değilse decimal göster
                        print(f"  Decimal değer: {HexValue}")
                    # bir önceki ile beraber toplanmasi gerekiyor ki toplam fiyat çiksin 
                elif self.BironcekiKomut == 0x12 and DataBytes[0] == 0x01 and DataBytes[1] == 0x3C:
                    print(f"POLL->AMOUNT data: {DataBytes.hex()} (len: {len(DataBytes)})")
                
                # READER komutları sonrası
                elif self.BironcekiKomut == 0x14 and DataBytes[0] == 0x00 and DataBytes[1] == 0x01:
                    print(f"READER->ENABLE_ACK data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif self.BironcekiKomut == 0x14 and DataBytes[0] == 0x00 and DataBytes[1] == 0x15:
                    print(f"READER->STATUS data: {DataBytes.hex()} (len: {len(DataBytes)})")
                
                # Diğer genel data paketleri  
                elif DataBytes[0] == 0x00 and DataBytes[1] == 0x00:
                    print(f"NULL/PADDING data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif DataBytes[0] == 0x00 and DataBytes[1] == 0x15:
                    print(f"CONTINUATION data: {DataBytes.hex()} (len: {len(DataBytes)})")
                elif DataBytes[0] == 0x00 and DataBytes[1] == 0x37:
                    print(f"PRICE/AMOUNT data: {DataBytes.hex()} (len: {len(DataBytes)})")
                    # Basit para hesaplama - sadece hex değerini decimal yap
                    HexValue = DataBytes[1]  # İkinci byte
                    if HexValue > 0:  # 0 değilse decimal göster
                        print(f"  Decimal değer: {HexValue}")
                elif DataBytes[0] == 0x00 and DataBytes[1] == 0x4B:
                    print(f"CONFIG/STATUS data: {DataBytes.hex()} (len: {len(DataBytes)})")
                    # Basit para hesaplama - sadece hex değerini decimal yap
                    HexValue = DataBytes[1]  # İkinci byte
                    if HexValue > 0:  # 0 değilse decimal göster
                        print(f"  Decimal değer: {HexValue}")
                elif DataBytes[0] == 0x01 and DataBytes[1] == 0x3C:
                    print(f"VALUE data: {DataBytes.hex()} (len: {len(DataBytes)})")
                
                else:
                    # Basit para hesaplama - sadece hex değerini decimal yap
                    HexValue = DataBytes[1]  # İkinci byte
                    if HexValue > 0:  # 0 değilse decimal göster
                        print(f"other bytes: {DataBytes.hex()} = {HexValue}")
                    else:
                        print(f"other bytes: {DataBytes.hex()} (len: {len(DataBytes)})")
        else:
            print(f"single byte: {DataBytes.hex()} (len: {len(DataBytes)})")
            
        if len(DataBytes) >= 2:
            ActualData = DataBytes[0]      # İlk byte: gerçek data
            ControlByte = DataBytes[1]     # İkinci byte: kontrol/9th bit
            
            # İkinci byte'ı incele
            NinthBit = 1 if (ControlByte & 0x01) else 0
            
            # 9-bit değer oluştur
            NineBitValue = (NinthBit << 8) | ActualData
            
            # Özel durumlar için kontrol
            if NinthBit:  # Command
                # Komut adını bul
                KomutAdi = "UNKNOWN"
                if ActualData == 0x10: KomutAdi = "RESET"
                elif ActualData == 0x11: KomutAdi = "SETUP" 
                elif ActualData == 0x12: KomutAdi = "POLL"
                elif ActualData == 0x13: KomutAdi = "VEND"
                elif ActualData == 0x14: KomutAdi = "READER"
                elif ActualData == 0x15: KomutAdi = "REVALUE"
                elif ActualData == 0x17: KomutAdi = "EXPANSION"
                
                if ActualData == 0x12:  # POLL komutu için özel frame
                    return AnalyzerFrame('poll_command', frame.start_time, frame.end_time, {})
                else:
                    return AnalyzerFrame('mdb_cmd', frame.start_time, frame.end_time, {
                        'hex_val': f"{NineBitValue:03X}",
                        'name': KomutAdi
                    })
            else:  # Data
                if ActualData == 0x00:  # ACK cevabı
                    return AnalyzerFrame('ack_response', frame.start_time, frame.end_time, {})
                else:
                    return AnalyzerFrame('mdb_data', frame.start_time, frame.end_time, {
                        'hex_val': f"{NineBitValue:03X}"
                    })
        else:
            # Tek byte varsa
            DataByte = DataBytes[0]
            return AnalyzerFrame('mdb_data', frame.start_time, frame.end_time, {
                'hex_val': f"{DataByte:02X}"
            })