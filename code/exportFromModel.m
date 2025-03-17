function exportFromModel(modelPath, outputPath, outputPrefix, exportFormats)
    % EXPORTFROMMODEL Loads a GEM from an XML or YML file and exports it in multiple formats.
    %
    % Usage:
    %   exportFromModel(modelPath, outputPath, outputPrefix)
    %   exportFromModel(modelPath, outputPath, outputPrefix, exportFormats)
    %
    % Inputs:
    %   modelPath     - Absolute path to the model file (e.g., 'iML1515.xml' or 'iML1515.yml')
    %   outputPath    - Directory where output files should be saved
    %   outputPrefix  - Prefix for output files (e.g., 'Ecoli-GEM')
    %   exportFormats - Cell array of formats (default: {'mat', 'txt', 'xlsx', 'xml', 'yml'})
    %
    % Example:
    %   exportFromModel('C:\path\to\iML1515.xml', 'C:\output\directory', 'Ecoli-GEM')

    if nargin < 4
        exportFormats = {'mat', 'txt', 'xlsx', 'xml', 'yml'}; % Default formats
    end

    % Ensure the file exists before proceeding
    if ~isfile(modelPath)
        error('Model file not found at: %s', modelPath);
    end

    % Determine the file format from the extension
    [~, ~, ext] = fileparts(modelPath);
    
    switch lower(ext)
        case '.xml'
            model = importModel(modelPath, false, false, false); % Load SBML model
        case '.yml'
            model = readYAMLmodel(modelPath, false); % Load YAML model
        otherwise
            error('Unsupported file format: %s. Use .xml or .yml', ext);
    end

    if isempty(model)
        error('Failed to load model. Check file path and format.');
    end

    %% Export Model in Multiple Formats
    exportForGit(model, ... % Ensure correct variable is used
                 outputPrefix, ...  % Prefix for output files
                 outputPath, ...  % Save in the specified directory
                 exportFormats, ...  % User-specified formats
                 false, ...  % mainBranchFlag (false for feature branches)
                 false, ...  % subDirs (organize into subdirectories)
                 false, ...  % COBRAtext (false to avoid COBRA-style text output)
                 false);     % neverPrefixIDs (false to keep standard IDs)

    disp('Model export complete. Files saved to:');
    disp(outputPath);
end
