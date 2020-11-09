# aws-ecr-findings-to-csv
Parses the JSON output of one or many images to a csv file

## inputJSONfile
This should be a properly formatted JSON file that contains one or more ECR image scan JSON outputs from the AWS ECR DescribeImageScanFindings API wrapped inside a single JSON block named "imageScans"

example (for a more detailed example see the [example-multiImageScan-results.json](./example-multiImageScan-results.json) file):
```
{
	"imageScans": [{
			"imageScanFindings": {
				"truncated": "... data of first image returned from DescribeImageScanFindings..."
			},
			"registryId": "123456789012",
			"repositoryName": "myrepo/prd/image1",
			"imageId": {
				"imageDigest": "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
				"imageTag": "latest"
			},
			"imageScanStatus": {
				"status": "COMPLETE",
				"description": "The scan was completed successfully."
			}
		},
		{
			"imageScanFindings": {
				"truncated": "... data of second image returned from DescribeImageScanFindings..."
			},
			"registryId": "123456789012",
			"repositoryName": "myrepo/prd/image2",
			"imageId": {
				"imageDigest": "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
				"imageTag": "latest"
			},
			"imageScanStatus": {
				"status": "COMPLETE",
				"description": "The scan was completed successfully."
			}
		}
	]
}
```
