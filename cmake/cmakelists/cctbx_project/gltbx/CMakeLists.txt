project(gltbx)

add_library( gltbx INTERFACE )
target_include_directories(gltbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/gltbx/font_ucs_10x20.cpp
            ${CMAKE_BINARY_DIR}/gltbx/font_ucs_8x13.cpp
            ${CMAKE_BINARY_DIR}/gltbx/font_ucs_9x15.cpp
            ${CMAKE_BINARY_DIR}/gltbx/FONTS_UCS_DONE_FLAG_FILE
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_00_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_01_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_02_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_03_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_04_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_05_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_06_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_defines_07_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_00_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_01_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_02_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_03_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_04_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_05_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_06_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_07_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_08_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_09_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_10_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_11_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_12_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_13_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_14_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/gl_functions_15_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_defines_00_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_defines_01_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_functions_00_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_functions_01_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_functions_02_bpl.cpp
            ${CMAKE_BINARY_DIR}/gltbx/glu_functions_03_bpl.cpp )

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_fonts_ext
              fonts_ext.cpp )
  add_generated_sources(gltbx_fonts_ext
              gltbx/font_ucs_8x13.cpp
              gltbx/font_ucs_9x15.cpp
              gltbx/font_ucs_10x20.cpp )
  target_link_libraries(gltbx_fonts_ext OpenGL::GL scitbx_boost_python)
endif()

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_gl_ext
              gl_ext.cpp )
  add_generated_sources(gltbx_gl_ext
              gltbx/gl_defines_00_bpl.cpp
              gltbx/gl_defines_01_bpl.cpp
              gltbx/gl_defines_02_bpl.cpp
              gltbx/gl_defines_03_bpl.cpp
              gltbx/gl_defines_04_bpl.cpp
              gltbx/gl_defines_05_bpl.cpp
              gltbx/gl_defines_06_bpl.cpp
              gltbx/gl_defines_07_bpl.cpp
              gltbx/gl_functions_00_bpl.cpp
              gltbx/gl_functions_01_bpl.cpp
              gltbx/gl_functions_02_bpl.cpp
              gltbx/gl_functions_03_bpl.cpp
              gltbx/gl_functions_04_bpl.cpp
              gltbx/gl_functions_05_bpl.cpp
              gltbx/gl_functions_06_bpl.cpp
              gltbx/gl_functions_07_bpl.cpp
              gltbx/gl_functions_08_bpl.cpp
              gltbx/gl_functions_09_bpl.cpp
              gltbx/gl_functions_10_bpl.cpp
              gltbx/gl_functions_11_bpl.cpp
              gltbx/gl_functions_12_bpl.cpp
              gltbx/gl_functions_13_bpl.cpp
              gltbx/gl_functions_14_bpl.cpp
              gltbx/gl_functions_15_bpl.cpp )
  target_link_libraries(gltbx_gl_ext OpenGL::GL scitbx_boost_python)
endif()

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_glu_ext
              glu_ext.cpp )
  add_generated_sources(gltbx_glu_ext
              gltbx/glu_defines_00_bpl.cpp
              gltbx/glu_defines_01_bpl.cpp
              gltbx/glu_functions_00_bpl.cpp
              gltbx/glu_functions_01_bpl.cpp
              gltbx/glu_functions_02_bpl.cpp
              gltbx/glu_functions_03_bpl.cpp )
  target_link_libraries(gltbx_glu_ext OpenGL::GL scitbx_boost_python)
endif()

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_quadrics_ext
              quadrics_ext.cpp )
  target_link_libraries(gltbx_quadrics_ext OpenGL::GL scitbx_boost_python)
endif()

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_viewer_utils_ext
              viewer_utils_ext.cpp )
  target_link_libraries(gltbx_viewer_utils_ext OpenGL::GL scitbx_boost_python)
endif()

if(TARGET OpenGL::GL)
  add_python_library ( gltbx_util_ext
              util_ext.cpp
              ../../gui_resources/gl2ps/gl2ps.c )
  target_link_libraries(gltbx_util_ext OpenGL::GL scitbx_boost_python)
endif()

