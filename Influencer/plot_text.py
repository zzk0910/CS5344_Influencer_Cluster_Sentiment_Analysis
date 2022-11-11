from bokeh.models import Div

# header
header = Div(text="""<h1>Visualization of Twitter Users</h1>""")

# project description
description = Div(text="""<p1>We include each influencer and its 2-nearest neighbours as one community. 
Nodes belonging to different communities are labelled by different colors[1-20]. We present the user id, user name, number of followers
and the recent sentiment of each user. The sentiment data come from the twitter sentiment analysis described before.</p1>""")

