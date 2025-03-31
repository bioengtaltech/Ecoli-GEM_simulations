function exportAnnotationsToTsv(modelPath, outputPath, exportAnnotations)
% ANNOTATIONTSV Exports a GEM model to tab-delimited annotation files.
%
% Usage:
%   exportAnnotationsToTsv(modelPath, outputPath, exportAnnotations)
%
% Inputs:
%   modelPath           - Absolute path to the SBML (.xml) model file
%   outputPath          - Directory where annotation files should be saved
%   exportAnnotations   - Cell array of annotation categories (default: {'rxns', 'mets', 'genes', 'model', 'comps'})
% Example:
%   exportAnnotationsToTsv('C:\path\to\iML1515.xml', 'C:\output\directory\', {'rxns', 'mets', 'genes', 'model', 'comps'})
%
% This function exports a GEM model into tab-delimited text files and
% then converts them to TSV format.

    if nargin < 3
        exportAnnotations = {'rxns', 'mets', 'genes', 'model', 'comps'}; % Default formats
    end

    % Validate input file exists
    if ~isfile(modelPath)
        error('Model file not found: %s', modelPath);
    end

    % Load SBML model
    model = importModel(modelPath, false, false, false);
    if isempty(model)
        error('Failed to load model from: %s', modelPath);
    end

    % Export model to tab-delimited text files
    exportToTabDelimited(model, outputPath, false);
    disp('Model exported to tab-delimited text files.');

    % Convert TXT files to TSV format based on exportAnnotations contents
    if ismember('rxns', exportAnnotations)
        movefile(strcat(outputPath, 'excelRxns.txt'), strcat(outputPath, 'rxns.tsv'));
        disp('rxns TXT file successfully converted to TSV format.');
    else
        delete(strcat(outputPath, 'excelRxns.txt'));
    end
    
    if ismember('mets', exportAnnotations)
        movefile(strcat(outputPath, 'excelMets.txt'), strcat(outputPath, 'mets.tsv'));
        disp('mets TXT file successfully converted to TSV format.');
    else
        delete(strcat(outputPath, 'excelMets.txt'));
    end
    
    if ismember('genes', exportAnnotations)
        movefile(strcat(outputPath, 'excelGenes.txt'), strcat(outputPath, 'genes.tsv'));
        disp('genes TXT file successfully converted to TSV format.');
    else
        delete(strcat(outputPath, 'excelGenes.txt'));
    end
    
    if ismember('model', exportAnnotations)
        movefile(strcat(outputPath, 'excelModel.txt'), strcat(outputPath, 'model.tsv'));
        disp('model TXT file successfully converted to TSV format.');
    else
        delete(strcat(outputPath, 'excelModel.txt'));
    end
    
    if ismember('comps', exportAnnotations)
        movefile(strcat(outputPath, 'excelComps.txt'), strcat(outputPath, 'comps.tsv'));
        disp('comps TXT file successfully converted to TSV format.');
    else
        delete(strcat(outputPath, 'excelComps.txt'));
    end

end
