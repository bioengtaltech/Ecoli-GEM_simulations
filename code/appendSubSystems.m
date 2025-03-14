function appendSubSystems(modelPathXml, modelPathMat, outputPath, outputPrefix)
% APPENDSUBSYSTEMS Adds the subSystems field from a MAT model to an XML model and exports it.
%
% Usage:
%   appendSubSystems(modelPathXml, modelPathMat, outputPath, outputPrefix)
%
% Inputs:
%   modelPathXml - Absolute path to the SBML (.xml) model file
%   modelPathMat - Absolute path to the MAT (.mat) model file containing subSystems data
%   outputPath   - Directory where the updated model should be saved
%   outputPrefix - Prefix for the output file
%
% Example:
%   appendSubSystems('C:\path\to\iML1515.xml', 'C:\path\to\iML1515.mat', 'C:\output\directory', 'iML1515_updated')

    % Validate input files exist
    if ~isfile(modelPathXml)
        error('SBML model file not found: %s', modelPathXml);
    end
    if ~isfile(modelPathMat)
        error('MAT model file not found: %s', modelPathMat);
    end

    % Load SBML model
    xmlModel = importModel(modelPathXml, false, false, false);
    if isempty(xmlModel)
        error('Failed to load SBML model from: %s', modelPathXml);
    end

    % Load MAT model
    matData = load(modelPathMat);
    if ~isfield(matData, 'iML1515')
        error('The MAT file does not contain a model structure.');
    end
    matModel = matData.iML1515;

    % Ensure the MAT model has a subSystems field
    if ~isfield(matModel, 'subSystems')
        error('The MAT model does not contain a subSystems field.');
    end

    % Extract relevant fields
    subSystems = matModel.subSystems;
    matRxns = matModel.rxns;
    xmlRxns = xmlModel.rxns;

    % Normalize reaction IDs in xmlRxns (remove 'R_' prefix if present)
    xmlRxnsClean = regexprep(xmlRxns, '^R_', '');

    % Ensure reactions match exactly
    if length(matRxns) == length(xmlRxnsClean) && all(strcmp(matRxns, xmlRxnsClean))
        xmlModel.subSystems = cellfun(@(x) {x}, subSystems, 'UniformOutput', false);
        disp('subSystems field successfully added to XML model.');
    else
        % Identify mismatches
        missingInXml = setdiff(matRxns, xmlRxnsClean);
        missingInMat = setdiff(xmlRxnsClean, matRxns);
        error(['Mismatch in reaction identifiers between models.\n', ...
               'Reactions missing in XML: %d\n', ...
               'Reactions missing in MAT: %d'], length(missingInXml), length(missingInMat));
    end

    % Export the updated model
    exportFormats = {'xml'};
    exportForGit(xmlModel, outputPrefix, outputPath, exportFormats, false, false, false, false);

    disp('Updated model exported successfully.');
end
