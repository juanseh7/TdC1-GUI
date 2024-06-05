import csv
import matplotlib.pyplot as plt

def read_csv(filename, vinPort, voutPort):
    # Check if the file extension is .csv
    if not filename.lower().endswith('.csv'):
        return None

    data = dict()

    data["t"] = []
    data["vin"] = []
    data["vout"] = []

    voutPortString = str(voutPort)
    vinPortString = str(vinPort)

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        cols = len(reader.fieldnames)

        if vinPort >= cols or voutPort >= cols:
            print("Port number exceeds the number of ports")
            return None
        for row in reader:
            if row["x-axis"] != "second":
                data["t"].append(float(row["x-axis"])*1e6 ) # Convert to microseconds
                if voutPort != 0:
                    data["vout"].append(float(row[voutPortString]))
                if vinPort != 0:
                    data["vin"].append(float(row[vinPortString]) )

    return data


def read_csv_bode(filename):
    data = dict()

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            for content in row.keys():
                if not content in data:
                    data[content] = []

                data[content].append(float(row[content]))
    return data

def parse_csv(filename, offset, vinPort, voutPort):
    data = read_csv(filename, vinPort, voutPort)

    if data is not None:
        # Apply offset to the data
        if data["vin"].__len__() > 0:
            vin_offset = [v + offset for v in data["vin"]]
            # Plot vin
            plt.plot(data["t"], 
                     vin_offset, 
                     label='Vin', 
                     # marker='o', 
                     color='red')
        if data["vout"].__len__() > 0:
            vout_offset = [v + offset for v in data["vout"]]
            # Plot vout
            plt.plot(data["t"], 
                     vout_offset, 
                     label='Vout', 
                     # marker='x', 
                     color='blue')

        # Adding titles and labels
        plt.title('Voltages over Time')
        plt.xlabel('Time $(\mu s)$')
        plt.ylabel('Voltage (V)')

        # Add a legend
        plt.legend()

        # Display the plot
        plt.grid(True)
        plt.show()

    else:
        print("The file is not a CSV file")