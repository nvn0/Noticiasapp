using Microsoft.AspNetCore.Mvc;

namespace Noticiasapp.Controllers
{
    public class IndexController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
