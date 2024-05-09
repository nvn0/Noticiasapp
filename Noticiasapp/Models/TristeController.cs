using Microsoft.AspNetCore.Mvc;

namespace Noticiasapp.Models
{
    public class TristeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
