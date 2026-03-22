set(PLUGIN_NAME gis_import)

qt_add_plugin(
    ${PLUGIN_NAME}
    SHARED
    gis_import.cpp
    gis_import.h
)

set_target_properties(
    ${PLUGIN_NAME}
    PROPERTIES
    AUTOMOC ON
    AUTOUIC ON
)

target_include_directories(${PLUGIN_NAME} PRIVATE
    ${PROJECT_SOURCE_DIR}/librecad/src/plugins
)

target_compile_definitions(${PLUGIN_NAME} PRIVATE
    DWGSUPPORT
    MUPARSER_STATIC
)

target_link_libraries(
    ${PLUGIN_NAME}
    PRIVATE
    Qt6::Core
    Qt6::Widgets
)

install(TARGETS ${PLUGIN_NAME}
    BUNDLE DESTINATION bin
    LIBRARY DESTINATION bin/resources/plugins
    RUNTIME DESTINATION bin/resources/plugins
)

if(WIN32)
    target_sources(${PLUGIN_NAME} PRIVATE gis_import.rc)
endif()
