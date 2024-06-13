import csv
import matplotlib.pyplot as plt

def read_csv(filename, v1Port, v2Port, v3Port, v4Port):
    # Check if the file extension is .csv
    if not filename.lower().endswith('.csv'):
        return None

    data = dict()

    data["t"] = []
    data["v1"] = []
    data["v2"] = []
    data["v3"] = []
    data["v4"] = []

    v1PortString = str(v1Port)
    v2PortString = str(v2Port)
    v3PortString = str(v3Port)
    v4PortString = str(v4Port)

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        cols = len(reader.fieldnames)

        if v1Port >= cols or v2Port >= cols or v3Port >= cols or v4Port >= cols:
            print("Port number exceeds the number of ports")
            return None
        for row in reader:
            if row["x-axis"] != "second":
                data["t"].append(float(row["x-axis"])*1e6 ) # Convert to microseconds
                if v1Port != 0:
                    data["v1"].append(float(row[v1PortString]))
                if v2Port != 0:
                    data["v2"].append(float(row[v2PortString]) )
                if v3Port != 0:
                    data["v3"].append(float(row[v3PortString]))
                if v4Port != 0:
                    data["v4"].append(float(row[v4PortString]) )

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

def graph_csv(filename, v1Port, v2Port, v3Port, v4Port, v1Offset, v2Offset, v3Offset, v4Offset, v1Multiplier, v2Multiplier, v3Multiplier, v4Multiplier):
    data = read_csv(filename, v1Port, v2Port, v3Port, v4Port)

    if data is not None:
        # Apply offset to the data
        if data["v1"].__len__() > 0:
            v1_offset = [v*v1Multiplier + v1Offset for v in data["v1"]]
            # Plot v1
            plt.plot(data["t"], 
                     v1_offset, 
                     label='v1', 
                     # marker='o', 
                     color='red')
        if data["v2"].__len__() > 0:
            v2_offset = [v*v2Multiplier + v2Offset for v in data["v2"]]
            # Plot v2
            plt.plot(data["t"], 
                     v2_offset, 
                     label='v2', 
                     # marker='x', 
                     color='blue')
        if data["v3"].__len__() > 0:
            v3_offset = [v*v3Multiplier + v3Offset for v in data["v3"]]
            # Plot v3
            plt.plot(data["t"], 
                     v3_offset, 
                     label='v3', 
                     # marker='x', 
                     color='green')
        if data["v4"].__len__() > 0:
            v4_offset = [v*v4Multiplier + v4Offset for v in data["v4"]]
            # Plot v4
            plt.plot(data["t"], 
                     v4_offset, 
                     label='v4', 
                     # marker='x', 
                     color='yellow')

        # Adding titles and labels
        plt.title('Voltages over Time')
        plt.xlabel('Time $(\mu s)$')
        plt.ylabel('Voltage (V)')

        xMin = min(data["t"])
        xMax = max(data["t"])

        # Remove excess graph
        plt.xlim([xMin, xMax])

        # Add a legend
        plt.legend()

        # Display the plot
        plt.grid(True)
        plt.show()

    else:
        print("The file is not a CSV file")