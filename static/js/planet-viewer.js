const viewer = document.querySelector("#planet-viewer");

if (viewer) {
    const canvas = document.querySelector("#planet-canvas");
    const status = document.querySelector("#planet-viewer-status");
    const resetButton = document.querySelector("#reset-planet-view");

    async function startPlanetViewer() {
        try {
            // Load Three.js and its rotation/zoom controls.
            const THREE = await import(
                "https://esm.sh/three@0.180.0"
            );

            const { OrbitControls } = await import(
                "https://esm.sh/three@0.180.0/examples/jsm/controls/OrbitControls.js"
            );

            // The scene is the 3D world containing our objects and lights.
            const scene = new THREE.Scene();

            // The camera determines what part of the 3D world we see.
            const camera = new THREE.PerspectiveCamera(
                45,
                viewer.clientWidth / viewer.clientHeight,
                0.1,
                100
            );

            camera.position.set(0, 0, 3.5);

            // The renderer draws the 3D world onto our HTML canvas.
            const renderer = new THREE.WebGLRenderer({
                canvas,
                alpha: true,
                antialias: true
            });

            renderer.setPixelRatio(
                Math.min(window.devicePixelRatio, 2)
            );

            renderer.setSize(
                viewer.clientWidth,
                viewer.clientHeight
            );

            renderer.outputColorSpace = THREE.SRGBColorSpace;

            // Create Jupiter's cloud-band texture.
            function createJupiterTexture() {
                const width = 2048;
                const height = 1024;

                const textureCanvas = document.createElement("canvas");
                textureCanvas.width = width;
                textureCanvas.height = height;

                const context = textureCanvas.getContext("2d");

                const colors = [
                    "#c18b60",
                    "#e5c9a0",
                    "#a96e4c",
                    "#ead6b0",
                    "#bd865c",
                    "#f0d9ad",
                    "#a86f51",
                    "#d6ad7e"
                ];

                // Horizontal bands form Jupiter's atmosphere.
                for (let y = 0; y < height; y += 3) {
                    const wave =
                        Math.sin(y * 0.035) +
                        Math.sin(y * 0.091) * 0.4;

                    const band = Math.floor(
                        (y / 48) + wave
                    );

                    const index =
                        (band % colors.length + colors.length) %
                        colors.length;

                    context.fillStyle = colors[index];
                    context.fillRect(0, y, width, 4);
                }

                // Add fine cloud streaks across the atmosphere.
                for (let i = 0; i < 650; i++) {
                    const y = Math.random() * height;
                    const startX = Math.random() * width;

                    context.beginPath();
                    context.moveTo(startX, y);

                    context.bezierCurveTo(
                        startX + 150, y - 8,
                        startX + 300, y + 8,
                        startX + 500, y
                    );

                    context.strokeStyle =
                        Math.random() > 0.5
                            ? "rgba(255, 239, 205, 0.16)"
                            : "rgba(77, 42, 30, 0.13)";

                    context.lineWidth = Math.random() * 5 + 1;
                    context.stroke();
                }

                // Draw the Great Red Spot.
                const spotX = width * 0.70;
                const spotY = height * 0.56;

                context.save();
                context.translate(spotX, spotY);
                context.rotate(-0.08);

                context.beginPath();
                context.ellipse(
                    0, 0, 145, 66, 0, 0, Math.PI * 2
                );
                context.fillStyle = "#a94e37";
                context.fill();

                context.beginPath();
                context.ellipse(
                    0, 0, 115, 43, 0, 0, Math.PI * 2
                );
                context.strokeStyle = "rgba(255, 205, 160, 0.55)";
                context.lineWidth = 8;
                context.stroke();

                context.beginPath();
                context.ellipse(
                    0, 0, 65, 22, 0, 0, Math.PI * 2
                );
                context.fillStyle = "rgba(112, 43, 35, 0.45)";
                context.fill();

                context.restore();

                const texture = new THREE.CanvasTexture(textureCanvas);
                texture.colorSpace = THREE.SRGBColorSpace;

                return texture;
            }

            // Create the sphere that represents Jupiter.
            const geometry = new THREE.SphereGeometry(
                1.15,
                96,
                64
            );

            const material = new THREE.MeshStandardMaterial({
                map: createJupiterTexture(),
                roughness: 1
            });

            const jupiter = new THREE.Mesh(geometry, material);
            jupiter.rotation.z = 0.04;
            scene.add(jupiter);

            // ------------------------------------------
            // JUPITER INTERACTIVE ANNOTATIONS
            // ------------------------------------------

            // This layer holds the clickable pointers.
            const annotationLayer = document.createElement("div");
            annotationLayer.className = "planet-annotation-layer";
            viewer.appendChild(annotationLayer);

            // The explanation panel appears beneath the viewer.
            const informationPanel = document.createElement("div");
            informationPanel.className = "planet-information-panel";
            informationPanel.innerHTML = `
                <span class="eyebrow">EXPLORE JUPITER</span>
                <h3>Select a feature</h3>
                <p>Choose any pointer on the planet to learn about that feature.</p>
            `;

            viewer.insertAdjacentElement("afterend", informationPanel);

            // Each feature has a position on Jupiter's surface.
            const features = [
                {
                    name: "Great Red Spot",
                    color: "#d66b50",
                    latitude: -22,
                    longitude: 65,
                    description:
                        "The Great Red Spot is a gigantic, long-lasting storm in Jupiter's atmosphere. It is an enormous rotating weather system that has been observed for centuries."
                },
                {
                    name: "Equatorial Bands",
                    color: "#c69a58",
                    latitude: 5,
                    longitude: 110,
                    description:
                        "These are alternating light and dark cloud bands around Jupiter's equator. They form because powerful atmospheric winds move in different directions."
                },
                {
                    name: "Atmosphere",
                    color: "#65a9cf",
                    latitude: 38,
                    longitude: 145,
                    description:
                        "Jupiter has a deep atmosphere made mainly of hydrogen and helium. Its clouds and powerful winds create the planet's changing appearance."
                },
                {
                    name: "Polar Regions",
                    color: "#8b9edb",
                    latitude: 72,
                    longitude: 25,
                    description:
                        "Jupiter's polar regions contain unusual atmospheric structures, including large collections of cyclones observed by NASA's Juno spacecraft."
                }
            ];

            const annotationMarkers = [];

            features.forEach((feature) => {
                const marker = document.createElement("button");

                marker.type = "button";
                marker.className = "planet-annotation";
                marker.textContent = feature.name;
                marker.setAttribute(
                    "aria-label",
                    `Learn about ${feature.name}`
                );

                marker.addEventListener("click", () => {
                    informationPanel.innerHTML = "";

                    const eyebrow = document.createElement("span");
                    eyebrow.className = "eyebrow";
                    eyebrow.textContent = "JUPITER FEATURE";

                    const heading = document.createElement("h3");
                    heading.textContent = feature.name;

                    const paragraph = document.createElement("p");
                    paragraph.textContent = feature.description;

                    informationPanel.append(
                        eyebrow,
                        heading,
                        paragraph
                    );

                    // Apply the selected feature's color to both.
                    informationPanel.style.setProperty(
                        "--feature-color",
                        feature.color
                    );

                    annotationMarkers.forEach(({ element }) => {
                        element.classList.remove("selected");
                        element.style.setProperty(
                            "--marker-color",
                            "transparent"
                        );
                    });

                    marker.classList.add("selected");
                    marker.style.setProperty(
                        "--marker-color",
                        feature.color
                    );
                });

                annotationLayer.appendChild(marker);

                // Convert latitude and longitude into a 3D position.
                const latitude = THREE.MathUtils.degToRad(
                    feature.latitude
                );

                const longitude = THREE.MathUtils.degToRad(
                    feature.longitude
                );

                const radius = 1.17;

                const position = new THREE.Vector3(
                    -radius * Math.cos(latitude) * Math.cos(longitude),
                    radius * Math.sin(latitude),
                    radius * Math.cos(latitude) * Math.sin(longitude)
                );

                annotationMarkers.push({
                    element: marker,
                    position
                });
            });

            // Project each 3D position onto the 2D screen.
            function updateAnnotations() {
                annotationMarkers.forEach(({ element, position }) => {
                    const worldPosition = jupiter.localToWorld(
                        position.clone()
                    );

                    const surfaceNormal = worldPosition.clone()
                        .sub(jupiter.position)
                        .normalize();

                    const directionToCamera = camera.position.clone()
                        .sub(worldPosition)
                        .normalize();

                    // Hide markers on the far side of Jupiter.
                    if (surfaceNormal.dot(directionToCamera) <= 0.08) {
                        element.style.display = "none";
                        return;
                    }

                    const projected = worldPosition.clone()
                        .project(camera);

                    if (projected.z > 1) {
                        element.style.display = "none";
                        return;
                    }

                    const x = (projected.x * 0.5 + 0.5)
                        * viewer.clientWidth;

                    const y = (-projected.y * 0.5 + 0.5)
                        * viewer.clientHeight;

                    element.style.display = "block";
                    element.style.left = `${x}px`;
                    element.style.top = `${y}px`;
                });
            }


            // Add lighting so the sphere has depth and shading.
            const ambientLight = new THREE.AmbientLight(
                0xffffff,
                1.2
            );

            scene.add(ambientLight);

            const sunlight = new THREE.DirectionalLight(
                0xffffff,
                2.5
            );

            sunlight.position.set(4, 2, 5);
            scene.add(sunlight);

            // Add distant stars around the planet.
            const starGeometry = new THREE.BufferGeometry();
            const starPositions = [];

            for (let i = 0; i < 450; i++) {
                starPositions.push(
                    (Math.random() - 0.5) * 18,
                    (Math.random() - 0.5) * 18,
                    (Math.random() - 0.5) * 18
                );
            }

            starGeometry.setAttribute(
                "position",
                new THREE.Float32BufferAttribute(starPositions, 3)
            );

            const starMaterial = new THREE.PointsMaterial({
                color: 0xffffff,
                size: 0.025
            });

            const stars = new THREE.Points(
                starGeometry,
                starMaterial
            );

            scene.add(stars);

            // OrbitControls provides dragging and zooming.
            const controls = new OrbitControls(
                camera,
                renderer.domElement
            );

            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.enablePan = false;
            controls.minDistance = 2.3;
            controls.maxDistance = 5;
            controls.rotateSpeed = 0.65;

            // Reset the camera and planet view.
            resetButton.addEventListener("click", () => {
                controls.reset();
                camera.position.set(0, 0, 3.5);
                jupiter.rotation.set(0, 0, 0.04);
            });

            // Keep the viewer correctly sized when its container changes.
            const resizeObserver = new ResizeObserver(() => {
                const width = viewer.clientWidth;
                const height = viewer.clientHeight;

                if (!width || !height) return;

                camera.aspect = width / height;
                camera.updateProjectionMatrix();

                renderer.setSize(width, height);
            });

            resizeObserver.observe(viewer);

            status.hidden = true;

            // Continuously draw the scene.
            renderer.setAnimationLoop(() => {
                controls.update();
                updateAnnotations();
                renderer.render(scene, camera);
            });

        } catch (error) {
            console.error("Jupiter viewer error:", error);

            status.textContent =
                "The 3D model could not load. Check your internet connection and refresh.";
        }
    }

    startPlanetViewer();
}
