class ChartDataset():
    def __init__(self, label, data, backgroundColor, borderColor):
        self.label = label
        self.data = data
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
    
    def export(self):
        return {
            "label": self.label,
            "data": self.data,
            "backgroundColor": self.backgroundColor,
            "borderColor": self.borderColor
        }

class ChartOptions():
    def __init__(self, maintainAspectRatio):
        self.maintainAspectRatio = maintainAspectRatio
    
    def export(self):
        return {
            "maintainAspectRatio": self.maintainAspectRatio
        }

class Chart():
    def __init__(self):
        self.type = "bar"
        self.data = {
            "labels": [],
            "datasets": []
        }
        self.options = {}
    
    def add_dataset(self, dataset):
        self.data["datasets"].append(dataset)
    
    def set_labels(self, labels):
        self.data["labels"] = labels
    
    def update_options(self, options):
        self.options.update(options)

    def export(self):
        return {
            "type": self.type,
            "data": self.data,
            "options": self.options
        }

class BarChart(Chart):
    def __init__(self):
        self.type = "bar"

class PieChart(Chart):
    def __init__(self):
        self.type = "pie"

class DoughnutChart(Chart):
    def __init__(self):
        self.type = "doughnut"