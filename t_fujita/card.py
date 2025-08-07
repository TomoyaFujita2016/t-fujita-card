import random
from typing import Optional

import typer
from terminaltexteffects.effects import (
    effect_beams,
    effect_binarypath,
    effect_blackhole,
    effect_bouncyballs,
    effect_bubbles,
    effect_burn,
    effect_crumble,
    effect_decrypt,
    effect_errorcorrect,
    effect_expand,
    effect_fireworks,
    effect_highlight,
    effect_laseretch,
    effect_matrix,
    effect_middleout,
    effect_orbittingvolley,
    effect_overflow,
    effect_pour,
    effect_print,
    effect_rain,
    effect_random_sequence,
    effect_rings,
    effect_scattered,
    effect_slice,
    effect_slide,
    effect_spotlights,
    effect_spray,
    effect_swarm,
    effect_sweep,
    effect_synthgrid,
    effect_unstable,
    effect_vhstape,
    effect_waves,
    effect_wipe,
)

app = typer.Typer()

# エフェクトのマッピング
EFFECTS_MAP = {
    "beams": effect_beams.Beams,
    "binarypath": effect_binarypath.BinaryPath,
    "blackhole": effect_blackhole.Blackhole,
    "bouncyballs": effect_bouncyballs.BouncyBalls,
    "bubbles": effect_bubbles.Bubbles,
    "burn": effect_burn.Burn,
    # "colorshift": effect_colorshift.ColorShift, # おもしろくないので
    "crumble": effect_crumble.Crumble,
    "decrypt": effect_decrypt.Decrypt,
    "errorcorrect": effect_errorcorrect.ErrorCorrect,
    "expand": effect_expand.Expand,
    "fireworks": effect_fireworks.Fireworks,
    "highlight": effect_highlight.Highlight,
    "laser": effect_laseretch.LaserEtch,
    "matrix": effect_matrix.Matrix,
    "middleout": effect_middleout.MiddleOut,
    "orbitting": effect_orbittingvolley.OrbittingVolley,
    "overflow": effect_overflow.Overflow,
    "pour": effect_pour.Pour,
    "print": effect_print.Print,
    "rain": effect_rain.Rain,
    "random": effect_random_sequence.RandomSequence,
    "rings": effect_rings.Rings,
    "scattered": effect_scattered.Scattered,
    "slice": effect_slice.Slice,
    "slide": effect_slide.Slide,
    "spotlights": effect_spotlights.Spotlights,
    "spray": effect_spray.Spray,
    "swarm": effect_swarm.Swarm,
    "sweep": effect_sweep.Sweep,
    "synthgrid": effect_synthgrid.SynthGrid,
    "unstable": effect_unstable.Unstable,
    "vhs": effect_vhstape.VHSTape,
    "waves": effect_waves.Waves,
    "wipe": effect_wipe.Wipe,
}


def create_card_text():
    """名刺のテキストコンテンツを作成"""
    content = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║             🌟 Tomoya Fujita / t-fujita 🌟               ║
║                                                          ║
║  💼 Work:      Software Engineer at 🏠 :)                ║
║  🏢 Company:   Grizzlarity Co., Ltd. (WIP)               ║
║  🚀 Freelance: PolarByters                               ║
║                                                          ║
║  ─────────────────────────────────────────────────────   ║
║                                                          ║
║  🌐 Company:   https://grizzlarity.com                   ║
║  💻 GitHub:    https://github.com/TomoyaFujita2016       ║
║  🐦 Twitter:   https://x.com/t_fujita24                  ║
║  📝 Zenn:      https://zenn.dev/tomoya_fujita            ║
║  📚 Qiita:     https://qiita.com/TomoyaFujita2016        ║
║  📦 PyPI:      https://pypi.org/user/t-fujita            ║
║                                                          ║
║  ─────────────────────────────────────────────────────   ║
║                                                          ║
║  📧 Contact:   fujita.t.works@gmail.com                  ║
║  💳 Card:      uvx t-fujita                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
    return content.strip()


def apply_effect(effect_name: str, text: str | None = None):
    """指定されたエフェクトを適用"""
    if effect_name not in EFFECTS_MAP:
        typer.echo(f"Error: Unknown effect '{effect_name}'")
        typer.echo(f"Available effects: {', '.join(EFFECTS_MAP.keys())}")
        raise typer.Exit(1)
    if text is None:
        text = create_card_text()

    effect_class = EFFECTS_MAP[effect_name]
    effect = effect_class(text)

    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


@app.command()
def main(
    effect: Optional[str] = typer.Argument(
        None,
        help=f"Effect to apply. Available: {', '.join(EFFECTS_MAP.keys())}",
        case_sensitive=False,
    ),
):
    """
    Display business card with terminal effects.

    Example:
        uvx t-fujita matrix
        uvx t-fujita fireworks
        uvx t-fujita  # random
    """

    effect = random.choice(list(EFFECTS_MAP.keys()))

    apply_effect(effect.lower())
    apply_effect(effect.lower(), f"effect: {effect.lower()}")


if __name__ == "__main__":
    app()
