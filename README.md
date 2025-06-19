# MDB Protocol Decoder v9

🚀 **Professional MDB (Multi-Drop Bus) Protocol Decoder for Saleae Logic Analyzer**

A comprehensive decoder that details MDB commands and parses internal data with advanced 9-bit to 2-byte conversion logic.

## 📸 Live Screenshots

The images above show the decoder in action:
- **Real-time MDB protocol analysis** with detailed command parsing
- **Enhanced timeline view** showing POLL/ACK cycles and VEND transactions  
- **Console output** with human-readable command descriptions and data values
- **Professional visualization** of vending machine communication protocols

A comprehensive decoder that details MDB commands and parses internal data with advanced 9-bit to 2-byte conversion logic.

## 🎯 Purpose

This decoder is designed to:
- **Detail MDB Commands**: Parse and identify all MDB protocol commands
- **Data Extraction**: Extract and interpret data from MDB packets
- **Enhanced Analysis**: Provide human-readable analysis of vending machine communications
- **Real-time Decoding**: Live analysis during protocol debugging

## ⚡ Key Features

### 🔧 Technical Capabilities
- **9-bit → 2 byte conversion**: Proper handling of MDB's unique data format
- **Packet length analysis**: Dynamic parsing based on packet size
- **Command-Response correlation**: Tracks command context for accurate response interpretation
- **Enhanced frame types**: Special analysis for critical operations

### 📊 Supported MDB Commands
| Command | Code | Description |
|---------|------|-------------|
| RESET | 0x10 | System reset command |
| SETUP | 0x11 | Device configuration |
| POLL | 0x12 | Status polling |
| VEND | 0x13 | Vending operations |
| READER | 0x14 | Card reader commands |
| REVALUE | 0x15 | Credit operations |
| EXPANSION | 0x17 | Extended features |

### 🎨 Enhanced Analysis
- **BEGIN_SESSION**: Detailed funds and level analysis
- **PERIPHERAL_ID**: Manufacturer and serial number extraction
- **VEND_APPROVED/DENIED**: Transaction amount parsing
- **READER_CONFIG**: Feature level and country code analysis

## 📖 Symbol Guide

When running the decoder, you'll see these symbols in the debug output:

| Symbol | Meaning | Description |
|--------|---------|-------------|
| `->` | ACK Response | Device acknowledges VMC command |
| `<-` | POLL Command | VMC polls device for status |

## 🚀 Installation

1. **Download** the `mdb_decoder.py` file
2. **Copy** to your Saleae Logic 2 extensions folder:
   - **Windows**: `%USERPROFILE%\Documents\Logic2Extensions`
   - **macOS**: `~/Documents/Logic2Extensions`
   - **Linux**: `~/Documents/Logic2Extensions`
3. **Restart** Saleae Logic 2
4. **Add Analyzer** → Search for "MDB Protocol Decoder"

## 🔌 Usage

### Basic Setup
1. Connect your logic analyzer to MDB bus
2. Set sampling rate to **1 MHz or higher**
3. Add the MDB Protocol Decoder to your data channel
4. Configure analyzer settings:
   - **Data Channel**: Select your MDB data line
   - **Clock Channel**: Select your MDB clock line (if available)

### Reading Results
The decoder provides multiple view formats:

#### 📱 Timeline View
- **POLL**: Simple poll commands
- **ACK**: Acknowledgment responses  
- **CMD: 0x113 (VEND)**: Detailed command info
- **DATA: 0x001**: Raw data packets
- **BEGIN SESSION - Funds: 500, Level: 1**: Enhanced analysis

#### 🖥️ Console Output
Detailed debug information including:
```
VEND bytes: 0113 (len: 2)
VEND->VEND_APPROVED response: 000500640000 (len: 6)
  Vend Amount: 100
```

## 📋 Example Output

### Typical MDB Transaction
```
<- POLL                     # VMC polls device
-> ACK                      # Device responds
CMD: 0x113 (VEND)          # VMC sends vend command  
VEND APPROVED - Amount: 150 # Device approves 150 cents
BEGIN SESSION - Funds: 500, Level: 1  # Session starts
```

### Card Reader Interaction
```
CMD: 0x114 (READER)
READER CONFIG - Level: 2, Country: 0x0840
PERIPHERAL ID - Mfg: ABC, SN: 12345678
```

## 🔧 Advanced Features

### Protocol Validation
- **Checksum verification**: Automatic validation of MDB checksums
- **Sequence tracking**: Monitors command-response pairs
- **Error detection**: Identifies protocol violations

### Data Analysis
- **Currency handling**: Automatic conversion of monetary values
- **Session tracking**: Follows complete transaction flows
- **Device identification**: Extracts manufacturer and model info

## 🛠️ Development

### Code Structure
```python
class Hla(HighLevelAnalyzer):
    def __init__(self):
        # Initialize decoder with startup message
        
    def decode(self, frame):
        # Main decoding logic
        # 1. Parse 2-byte packets into 9-bit values
        # 2. Identify command vs data
        # 3. Apply context-aware analysis
        # 4. Return enhanced frame
```

### Key Components
- **9-bit Conversion**: `_GetNineBitDeger()` handles bit manipulation
- **Command Tracking**: `BironcekiKomut` maintains state
- **Enhanced Parsing**: Specialized functions for each response type

## 📚 MDB Protocol Reference

### Packet Structure
```
[Data Byte][Control Byte]
    |           |
    |           └── Bit 0: Command/Data flag
    |               Bit 1-7: Reserved
    └── 8-bit payload data
```

### 9-bit Value Format
```
Bit 8: Command flag (1=Command, 0=Data)
Bit 7-0: Actual data/command code
```








![image](https://github.com/user-attachments/assets/22a23bdf-b255-4400-b75b-2aa334202353)
![image](https://github.com/user-attachments/assets/b07159b1-9819-449b-b632-81263b228653)

![image](https://github.com/user-attachments/assets/1a724ec8-8745-4392-93c1-129e8f91c481)
















## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Bug Reports**: Found an issue? Open an issue with details
2. **💡 Feature Requests**: Have ideas? Let us know!
3. **🔧 Code Contributions**: Fork, improve, and submit PRs
4. **📖 Documentation**: Help improve this README

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 👨‍💻 Author

**ByTaymur**
- GitHub: [@ByTaymur](https://github.com/ByTaymur)
- Specialization: Embedded systems, protocol analysis, vending machine technology

## 🙏 Acknowledgments

- **Saleae Team**: For the excellent Logic Analyzer platform
- **MDB Community**: For protocol documentation and support
- **Vending Industry**: For real-world testing scenarios

## 📞 Support

Having issues? Here's how to get help:

1. **📖 Check Documentation**: Review this README thoroughly
2. **🔍 Search Issues**: Look for existing solutions
3. **💬 Open Issue**: Create detailed bug report
4. **📧 Contact**: Reach out via GitHub

---

⭐ **Star this project if it helped you!** ⭐

*Made with ❤️ for the embedded systems community*
