import plotly.express as px


def create_bar_chart(metrics):
    data = {
        'Metric': ['Avg Duration (min)', 'Avg Tip (%)'],
        'Value': [metrics['avg_duration'], metrics['avg_tip_pct']]
    }
    
    fig = px.bar(
        data, 
        x='Metric', 
        y='Value',
        color='Value',
        color_continuous_scale=['#1E6FCC', '#C45C3A'],
        text_auto='.1f'
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family='Outfit',
        showlegend=False,
        font=dict(color='#F0F3F6', size=18),
        xaxis=dict(
            showgrid=False, 
            title="", 
            tickfont=dict(color='#F0F3F6', size=16)
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='#30363D', 
            title="", 
            tickfont=dict(color='#F0F3F6', size=14)
        )
    )
    fig.update_traces(
        marker=dict(line=dict(color='#242B35', width=1)),
        textposition='auto',
        textfont=dict(color='#F0F3F6', size=16)
    )
    
    return fig


def create_pie_chart(metrics):
    data = {
        'Category': ['Fare', 'Duration', 'Tip %', 'Revenue'],
        'Value': [
            metrics['avg_fare'], 
            metrics['avg_duration'], 
            metrics['avg_tip_pct'], 
            metrics['total_revenue']/1e8
        ]
    }
    
    fig = px.pie(
        data, 
        values='Value', 
        names='Category',
        color_discrete_sequence=['#1E6FCC', '#C45C3A', '#4FA85B', '#8E6B8E']
    )
    
    fig.update_layout(
        font_family='Outfit',
        font=dict(color='#F0F3F6', size=18),
        showlegend=True,
        legend=dict(
            orientation="h", 
            yanchor="bottom", 
            y=-0.15, 
            xanchor="center", 
            x=0.5, 
            font=dict(color='#F0F3F6', size=16)
        )
    )
    fig.update_traces(
        textfont=dict(color='#F0F3F6', size=16),
        marker=dict(line=dict(color='#0F1419', width=2))
    )
    
    return fig