# Netrun landscape plugin build configuration
# Included when BUILD_LANDSCAPE_PLUGINS=ON

include_directories(
    ${PROJECT_SOURCE_DIR}/librecad/src/plugins
)

add_subdirectory(gis_import)
add_subdirectory(kiri_import)
add_subdirectory(plant_database)
add_subdirectory(irrigation)
