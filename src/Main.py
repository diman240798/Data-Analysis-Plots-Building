from src.CSVExaminer import examineCSVbyName
from src.PlotBuilder import plotByTeamName
import src.Config as Config

examineCSVbyName(Config.incomeCSV)
plotByTeamName('ЦСКА')