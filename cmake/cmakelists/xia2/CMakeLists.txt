project(xia2)

add_library( xia2 INTERFACE )
target_include_directories(xia2 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_subdirectory(Modules)
