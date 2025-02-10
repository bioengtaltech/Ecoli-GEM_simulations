import memote.suite.api as memote_api
import cobra

# Read model
model = cobra.io.read_sbml_model('model/iML1515.xml')

# Run memote test
_, result = memote_api.test_model(model, exclusive=None, skip=None, results=True)

# Generate html report
html_report = memote_api.snapshot_report(result)


# Save html report
report_path = 'memote_report.html'
with open(report_path, 'w', encoding='utf-8') as file:
    file.write(html_report)
