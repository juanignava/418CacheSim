import PySimpleGUI as sg
from Obtener_Graficas import *

if __name__ == '__main__':
    # Constants & Variables
    
    bench_list = ["MSI_vs_MESI", "MSI_vs_MOSI", "MOESI_vs_Dragon", "Lock_Add" , "Lock_Fill_Bucket", "Wild_Fill_Bucket"]

    # UI element declaration
    sg.theme("SandyBeach")

    title = sg.Text(text="Visualizador de resultados para pruebas", font="none 16 bold")
    title2 = sg.Text(text="de protocolos de coherencia de caché", font="none 16 bold")
    title_down = sg.Text(text="2022. J.I Navarro & J.D Sánchez", font="none 12")

    separator_top = sg.HorizontalSeparator(color="white", pad=12)

    #For BP
    subtitle_branchPredictor = sg.Text(text="Resultados sobre algoritmo específico", font="noce 13 bold italic", size=31)
    
    subtitle_bench = sg.Text(text="Algoritmo:", font="none 13 italic", size=10)
    combo_bench = sg.Combo(values=bench_list, enable_events=True, default_value=bench_list[0], key="key_combo_code", readonly=True, size=22)
    
    show_BP_button = sg.Button(button_text="Mostrar Gráfica", key="key_show_graph_button", font="none 14 bold",  size=23)

    separator_middle = sg.HorizontalSeparator(color="white", pad=12)

    # Define layout of UI elements
    layout = [[title],[title2],
              [title_down],

              #For BP
              [separator_top],
              [subtitle_branchPredictor],
              [subtitle_bench, combo_bench],
              [show_BP_button]]

    # Start window
    window = sg.Window("Visualizador de resultados", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        
        if event == "key_show_graph_button":
            # Get values
            code = values["key_combo_code"]
            
            graficarDatos(code)

    window.close()