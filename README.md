
# 3D Rectangular Prism Viewer

This application allows users to visualize and analyze 3D models of rectangular prisms. It uses PyQt5 for the GUI and PythonOCC for 3D CAD visualization.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/RectangularPrismViewer.git
   ```

2. Navigate to the project directory:
   ```
   cd RectangularPrismViewer
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python main.py
   ```

2. Use the dropdown menu to select a prism.
3. View the calculated surface area and volume.
4. Click the "Visualize 3D Model" button to see the 3D representation of the prism.

## Development

- `main.py`: Contains the main application logic and GUI setup.
- `prism_calculator.py`: Includes the PrismCalculator class for surface area and volume calculations.
- `draw_rectangular_prism.py`: Contains functions for creating 3D prism shapes.
- `prisms.db`: SQLite database storing prism dimensions.

## Creating an Executable

To create an executable, use PyInstaller:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --onefile --windowed main.py
   ```

The executable will be created in the `dist` directory.

## License

This project is licensed under the MIT License.
