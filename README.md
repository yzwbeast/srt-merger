# srt-merger

[中文版本 README available here](README.zh.md)

**SRT Merger** is a simple Python script designed for the sequential amalgamation of multiple `.srt` subtitle files. It automatically sorts the subtitle files based on the numeric sequence within their filenames, thereby ensuring they are merged in the correct order and the subtitle indices are appropriately updated.

## Overview of Features

- Automatically sorts subtitle files according to the numerical order in their filenames (e.g., `001`, `002`, `003`).
- Merges all `.srt` files while preserving timestamps and subtitle content.
- Updates the subtitle indices to ensure continuity within the merged file.

## Usage Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/srt-merger.git
   cd srt-merger
   ```

2. **Prepare Your .srt Files**  
   Place all the `.srt` files you wish to merge into a single directory (e.g., `./sss`).

3. **Modify the Script's Folder Path**  
   Ensure the `folder_path` variable in the script is set to the path of the directory containing your `.srt` files.
   ```bash
   folder_path = "./sss"  # Modify to your directory path
   ```

4. **Run the Script**  
   Execute the Python script; the merged subtitle file will be saved as `merged.srt`.
   ```bash
   python main.py
   ```

5. **Output File**  
   The merged subtitle file will be saved in the directory where the script resides, named `merged.srt`.

## Installation Requirements

- Python 3.x
- No additional libraries required

## Contributions

Contributions are welcome! Please submit [issues](https://github.com/yzwbeast/srt-merger/issues) or pull requests to enhance the project!

## License

This project is licensed under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.

[中文版本 README available here](README.zh.md)
