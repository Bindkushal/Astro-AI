import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord, AltAz
from astropy.time import Time
from astropy.coordinates import EarthLocation
import astropy.units as u

# Set up the location and time (New York City as an example)
location = EarthLocation(lat=40.7128 * u.deg, lon=-74.0060 * u.deg)
time = Time.now()

# Define the star's celestial coordinates (Right Ascension and Declination)
star_coord = SkyCoord(ra=10 * u.deg, dec=20 * u.deg, frame='icrs')

# Convert the star's coordinates to AltAz (Altitude, Azimuth)
altaz_frame = AltAz(obstime=time, location=location)
star_altaz = star_coord.transform_to(altaz_frame)

# Plot the star's position on a 2D graph (Azimuth vs Altitude)
plt.figure(figsize=(6,6))
plt.scatter(star_altaz.az.deg, star_altaz.alt.deg, color='yellow', s=100, label="Star")

# Add labels and title
plt.xlabel("Azimuth (degrees)")
plt.ylabel("Altitude (degrees)")
plt.title("Star's Position in the Sky")
plt.xlim(0, 360)
plt.ylim(0, 90)

# Add a star symbol
plt.scatter(star_altaz.az.deg, star_altaz.alt.deg, color='yellow', s=200, marker='*')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()
