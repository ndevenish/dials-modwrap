project(prime)

add_library( prime INTERFACE )
target_include_directories(prime INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( prime_ext
            ext.cpp )
target_link_libraries(prime_ext cctbx scitbx_boost_python)

add_subdirectory(index_ambiguity)
