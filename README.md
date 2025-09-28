# About dashboard

This dashboard is created using [ScholarImpact](https://github.com/abhishektiwari/scholarimpact) - a bibliometric tool to analyse, visualise, and share your research impact, output and scholarly influence using Google Scholar and OpenAlex data.

# Running as Docker container

```
docker build -t scholarimpact-dashboard .
docker run -p 8501:8501 scholarimpact-dashboard 
```

As background process,

```
docker run -d -p 8501:8501 --name scholarimpact-dashboard scholarimpact-dashboard
```

Stopping and removing

```
docker ps
docker stop  scholarimpact-dashboard
docker rm scholarimpact-dashboard
```