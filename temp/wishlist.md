
# List of items to complete

Hi Eric and Jonathan, I had a nice chat with Boyce Griffiths, the leader of the IBAMR project. Notes from the conversation are below.

What do you think? One option is that, next time we meet, we draft an e-mail to Boyce together, that very specifically explains what we want to do. This is especially for Point 5abc below.

Notes from chat with Boyce 19 May 2021

1. In principle, our idea of running the simulation to steady-state, extracting the structure points, and starting them back up should yield a stable simulation. Why isn't it working? Maybe it wasn't run long enough to a true steady state. Are the velocity fields close enough to zero?
    Can't parse out data from the vtk files
    Should check export script and review IBAMR docs.

2. Boyce watched the gif and immediately pointed out the high-frequency oscillations at the sides of the right cell. He thinks we should prioritize getting rid of those, because they are a sign of numerical issues.
• Could this be due to the spacing of structure points? See next point.

3. The spacing of the structure points (i.e., the cell envelope) is a key numerical parameter that we need to choose carefully. The structure lives on a certain mesh that is specified in level_number = MAX_LEVELS - 1 (currently input2d line 113), and the adaptive mesh just makes sure it's always on that mesh near the structure. At this mesh size, structure points should be approximately the same spacing as the mesh size -- around 0.5x or 1x or 1.5x.
• This might solve permeability problems, i.e., it might make the structure more impermeable, which is what we want.
    Run multiple identical simulations, changing spacing

4. One of our goals is to get closer to physiological parameters (rho, mu, etc). Boyce suggested setting rho=0. He said he doesn't think the algorithm will choke. This would be great because it would remove a parameter. It might make the computation more stable or less stable...
    Try running with rho set to 0
    If run at current dt, could you increase dt tenfold, etc.?

5. Things that Boyce says can be adjusted by editing the input files:
• a) We can add a point force on each structure vertex
• b) We can add a background flow
• c) We can add boundary conditions on the flow, e.g., inwards on left-right and outwards on top-bottom, which would induce a background flow
    Things we still haven't figured out how to do
    Aspirations to go 3D

6. Things that require editing the C++ code:
• A nonlinear spring or dynamic linkages (that change depending on structure position, e.g., proximity of the cells)

7. He mentioned they want to work on a docker/singularity container but haven't gotten around to it. I wonder if we can help by showing them ours, when we feel it's ready.
    Share Docker Hub (Poorvi)
    Make the README in the github readable (Or at least relevent to new code)
    Store data not in github but in Google Drive or somewhere else
        UCI Google Drive, rclone
