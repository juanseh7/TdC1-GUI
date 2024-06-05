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
        if len(reader.fieldnames) == 5:
            if vinPort > 4 or voutPort > 4:
                print("Port number exceeds the number of ports")
                return None
            if vinPort == 0:
                vinPortString = "3"
            if voutPort == 0:
                voutPortString = "1"
            for row in reader:
                if row["x-axis"] != "second":
                    data["t"].append(float(row["x-axis"])*1e6 ) # Convert to microseconds
                    data["vout"].append(float(row[voutPortString]) )
                    data["vin"].append(float(row[vinPortString]) )
        else:
            if vinPort > 2 or voutPort > 2:
                print("Port number exceeds the number of ports")
                return None
            if vinPort == 0:
                vinPortString = "2"
            if voutPort == 0:
                voutPortString = "1"
            for row in reader:
                if row["x-axis"] != "second":
                    data["t"].append(float(row["x-axis"])*1e6 ) # Convert to microseconds
                    data["vout"].append(float(row[voutPortString]) )
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
        vin_offset = [v + offset for v in data["vin"]]
        vout_offset = [v + offset for v in data["vout"]]

        # Create a plot
        #plt.figure(figsize=(10, 6))

        # Plot vin
        plt.plot(data["t"], vin_offset, label='Vin', marker='o', color='red')

        # Plot vout
        plt.plot(data["t"], vout_offset, label='Vout', marker='x', color='blue')

        # Adding titles and labels
        plt.title('Vin and Vout over Time')
        plt.xlabel('Time $(\mu s)$')
        plt.ylabel('Voltage (V)')

        # Add a legend
        plt.legend()

        # Display the plot
        plt.grid(True)
        plt.show()

    else:
        print("The file is not a CSV file")