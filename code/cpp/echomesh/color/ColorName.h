#ifndef __ECHOMESH_COLOR_COLORNAME__
#define __ECHOMESH_COLOR_COLORNAME__

#include "echomesh/base/Echomesh.h"

namespace echomesh {

class FColor;

namespace color {

bool nameToRgb(const String& cname, FColor*);
string rgbToName(const FColor&);

}  // namespace color
}  // namespace echomesh

#endif  // __ECHOMESH_COLOR_COLORNAME__
