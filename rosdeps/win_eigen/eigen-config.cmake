
get_filename_component(Eigen_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)

set(Eigen_VERSION 3.2.1 CACHE INTERNAL "")
set(Eigen_INCLUDE_DIR "${Eigen_CMAKE_DIR}/../../../include/eigen3" CACHE PATH "Eigen include directory")
set(Eigen_INCLUDE_DIRS "${Eigen_INCLUDE_DIR}" CACHE INTERNAL "")
set(Eigen_LIBRARY_DIRS "" CACHE INTERNAL "")
set(Eigen_LIBRARIES "" CACHE INTERNAL "")
