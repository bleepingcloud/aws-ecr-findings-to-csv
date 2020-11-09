import json
import csv

inputJSONfile = "input.json"
outputCSVfile = "output.csv"


def parse_scan_results():
    """Iterates through the Multi-image scan results and parses out relevant info"""
    
    try:        
        with open(inputJSONfile) as f:
            scanData = json.load(f)
        findingItemsList = []
        images = scanData['imageScans']
        for image in images:
            imageRepo = image['repositoryName']
            imageTag = image['imageId']['imageTag']
            findings = image['imageScanFindings']['findings']
            scanSummary = image['imageScanFindings']['findingSeverityCounts']
            for finding in findings:
                findingItem = {}
                name  = finding['name']
                severity = finding['severity']
                description = finding['description']
                uri = finding['uri']
                findingItem["image"] = imageRepo + ':' + imageTag
                findingItem["name"] = name
                findingItem["severity"] = severity
                findingItem["description"] = description
                findingItem["uri"] = uri
                findingItemsList.append(findingItem)
        return findingItemsList
        
            
    except FileNotFoundError:
        print("Could not find the source JSON file")

def generate_csv():
    csv_columns = ['image', 'name', 'severity', 'description', 'uri']
    
    try:
        with open(outputCSVfile, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in parse_scan_results():
                writer.writerow(data)
    except IOError:
        print("I/O error")

print (parse_scan_results())
generate_csv()
