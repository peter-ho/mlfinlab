"""
Package based on the text book: Advances in Financial Machine Learning, by Marcos Lopez de Prado
"""
import webbrowser
import textwrap

import mlfinlab.cross_validation as cross_validation
import mlfinlab.data_structures as data_structures
import mlfinlab.multi_product as multi_product
import mlfinlab.filters.filters as filters
import mlfinlab.labeling.labeling as labeling
import mlfinlab.features.fracdiff as fracdiff
import mlfinlab.sample_weights as sample_weights
import mlfinlab.sampling as sampling
import mlfinlab.bet_sizing as bet_sizing
import mlfinlab.util as util
import mlfinlab.structural_breaks as structural_breaks
import mlfinlab.feature_importance as feature_importance
import mlfinlab.ensemble as ensemble
import mlfinlab.portfolio_optimization as portfolio_optimization
import mlfinlab.clustering as clustering
import mlfinlab.backtest_statistics.statistics as backtest_statistics


# Sponsorship notification
# try:
#     webbrowser.get('google-chrome').open('https://www.patreon.com/HudsonThames', new=2)
# except webbrowser.Error as error:
#     try:
#         webbrowser.get('firefox').open('https://www.patreon.com/HudsonThames', new=2)
#     except webbrowser.Error as error:
#         try:
#             webbrowser.get('windows-default').open('https://www.patreon.com/HudsonThames', new=2)
#         except webbrowser.Error as error:
#             pass

print()
print(textwrap.dedent("""slack channel using the following link: https://join.slack.com/t/mlfinlab/shared_invite/zt-c62u9gpz-VFc13j6da~UVg3DkV7~RjQ"""))
print()
