
interface GPXData {
    metadata: { name?: string };
    waypoints: GPXWaypoint[];
    tracks: GPXTrack[];
}

interface GPXWaypoint {
    lat: number;
    lon: number;
    name?: string;
}

interface GPXTrack {
    name?: string;
    segments: GPXSegment[];
}

interface GPXSegment {
    points: GPXPoint[];
}

interface GPXPoint {
    lat: number;
    lon: number;
    ele?: number;
    time?: string;
}



export class GpxParser {

    static gpxIsValid(gpx: string) {
        try {

            const gpxData: GPXData = {
                metadata: {},
                waypoints: [],
                tracks: [],
            };

            const metadataMatch = gpx.match(/<metadata>([\s\S]*?)<\/metadata>/);
            if (metadataMatch) {
                gpxData.metadata.name = metadataMatch[1].match(/<name>([\s\S]*?)<\/name>/)[1];
            }

            const waypointMatches = gpx.match(/<wpt.*?<\/wpt>/gs);
            if (waypointMatches) {
                waypointMatches.forEach((waypointMatch) => {
                    const waypoint: GPXWaypoint = {
                        lat: parseFloat(waypointMatch.match(/lat="([-0-9.]+)"/)![1]),
                        lon: parseFloat(waypointMatch.match(/lon="([-0-9.]+)"/)![1]),
                    };
                    const nameMatch = waypointMatch.match(/<name>([\s\S]*?)<\/name>/);
                    if (nameMatch) {
                        waypoint.name = nameMatch[1];
                    }
                    gpxData.waypoints.push(waypoint);
                });
            }

            const trackMatches = gpx.match(/<trk>[\s\S]*?<\/trk>/gs);
            if (trackMatches) {
                trackMatches.forEach((trackMatch) => {
                    const track: GPXTrack = {
                        segments: [],
                    };
                    const nameMatch = trackMatch.match(/<name>([\s\S]*?)<\/name>/);
                    if (nameMatch) {
                        track.name = nameMatch[1];
                    }

                    const segmentMatches = trackMatch.match(/<trkseg>[\s\S]*?<\/trkseg>/gs);
                    if (segmentMatches) {
                        track.segments = segmentMatches.map((segmentMatch) => {
                            const segment: GPXSegment = {
                                points: [],
                            };
                            const pointMatches = segmentMatch.match(/<trkpt.*?<\/trkpt>/gs);
                            if (pointMatches) {
                                pointMatches.forEach((pointMatch) => {
                                    const point: GPXPoint = {
                                        lat: parseFloat(pointMatch.match(/lat="([-0-9.]+)"/)![1]),
                                        lon: parseFloat(pointMatch.match(/lon="([-0-9.]+)"/)![1]),
                                    };
                                    const eleMatch = pointMatch.match(/<ele>([-0-9.]+)<\/ele>/);
                                    if (eleMatch) {
                                        point.ele = parseFloat(eleMatch[1]);
                                    }
                                    const timeMatch = pointMatch.match(/<time>([\s\S]*?)<\/time>/);
                                    if (timeMatch) {
                                        point.time = timeMatch[1];
                                    }
                                    segment.points.push(point);
                                });
                            }
                            return segment;
                        });
                    }

                    gpxData.tracks.push(track);
                });
            }

            //Provera
            if (gpxData.tracks.length === 0) {
                return false;
            }

            for (const track of gpxData.tracks) {
                if (!track.name) {
                    return false
                }

                if (track.segments.length === 0) {
                    return false
                }

                for (const segment of track.segments) {
                    for (const point of segment.points) {
                        if (point.lat < -90 || point.lat > 90 || point.lon < -180 || point.lon > 180) {
                            return false
                        }
                    }
                }
            }

        } catch (error) {
            return false;
        }

        return true;
    }
}